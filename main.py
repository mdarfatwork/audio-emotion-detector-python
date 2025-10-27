import torch
import librosa
from transformers import AutoModelForAudioClassification, AutoFeatureExtractor
from pathlib import Path

# Load model + feature extractor
model_name = "superb/hubert-large-superb-er"
extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = AutoModelForAudioClassification.from_pretrained(model_name)

# Emotion label mapping
LABEL_MAP = {
    "hap": "Happy 😊",
    "sad": "Sad 😢",
    "ang": "Angry 😠",
    "neu": "Neutral 😐"
}

# Function to predict emotion from audio file
def predict_emotion(audio_path):
    speech, sr = librosa.load(audio_path, sr=16000)
    inputs = extractor(speech, sampling_rate=16000, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_id = torch.argmax(logits, dim=-1).item()
    label = model.config.id2label[predicted_id]
    emotion = LABEL_MAP.get(label, label)
    return f"{Path(audio_path).name}: Detected Emotion -> {emotion}"

# Test on local sample audio files
if __name__ == "__main__":
    sample_folder = Path("samples")
    for audio_file in sample_folder.glob("*.mp3"):
        result = predict_emotion(audio_file)
        print(result)
