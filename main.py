import torch
import librosa
from transformers import AutoModelForAudioClassification, AutoFeatureExtractor
import gradio as gr

# Load model + feature extractor
model_name = "superb/hubert-large-superb-er"
extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = AutoModelForAudioClassification.from_pretrained(model_name)

# Function: predict emotion
LABEL_MAP = {
    "hap": "Happy 😊",
    "sad": "Sad 😢",
    "ang": "Angry 😠",
    "neu": "Neutral 😐"
}

def predict_emotion(audio_path):
    speech, sr = librosa.load(audio_path, sr=16000)
    inputs = extractor(speech, sampling_rate=16000, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_id = torch.argmax(logits, dim=-1).item()
    label = model.config.id2label[predicted_id]
    emotion = LABEL_MAP.get(label, label)
    return f"Detected Emotion: {emotion}"

# Simple Gradio UI
app = gr.Interface(
    fn=predict_emotion,
    inputs=gr.Audio(type="filepath", label="Upload or Record Audio"),
    outputs="text",
    title="🎧 Audio Emotion Detector",
    description="Upload a short speech audio clip and detect emotion (happy, sad, angry, neutral)."
)

if __name__ == "__main__":
    app.launch()
