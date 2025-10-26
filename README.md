# 🎧 Audio Emotion Detector

A simple **AI-powered Python project** that detects emotions from short **speech audio clips**.

Upload or record an audio sample (like someone talking), and the model predicts whether the emotion is **Happy**, **Sad**, **Angry**, or **Neutral** — all in real time.

---

## 🚀 Features

- 🎵 Upload or record any short audio (speech)
- 🧠 Uses a **pretrained Hugging Face model**: `superb/hubert-large-superb-er`
- 💡 Detects emotions: `Happy`, `Sad`, `Angry`, `Neutral`
- 🧩 Built with: `Python`, `librosa`, `transformers`, `torch`, `gradio`
- ⚙️ No training required — works instantly
- 🌐 Optional web interface with **Gradio**

---

## 🛠️ Tech Stack

| Component | Description |
|-----------|-------------|
| **Python** | Main language |
| **librosa** | For loading and processing audio |
| **transformers** | Loads pretrained Hugging Face model |
| **torch** | Deep learning backend for inference |
| **gradio** | For building an interactive UI |

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mdarfatwork/audio-emotion-detector-python.git
cd audio-emotion-detector-python
```

### 2️⃣ Create and activate a virtual environment (recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the app

```bash
python main.py
```

After running, a Gradio interface will open in your browser. You can either:

- 🎙️ Record audio directly, or
- 📁 Upload a `.wav` / `.mp3` file

The app will display the predicted emotion.

---

## 🧠 Model Info

This project uses the Hugging Face model: **superb/hubert-large-superb-er**

Trained on the IEMOCAP dataset, it recognizes:

- `hap` → Happy 😊
- `sad` → Sad 😢
- `ang` → Angry 😠
- `neu` → Neutral 😐

---

## 📁 Project Structure

```
audio-emotion-detector/
│
├── main.py     # Main Python script
├── requirements.txt              # Locked dependencies
├── README.md                     # Project documentation
└── samples/                      # Example audio files
```

---

## 💡 Example Output

```
Detected Emotion: Happy 😊
```

---

## ⚠️ Notes

- For best results, use short clips (2–5 seconds) with clear speech.
- The model works best for English speech.
- No GPU is required — works fine on CPU.

---

## 📜 License

This project is open-source and free to use for educational or personal purposes.

**Model credit:** Hugging Face - [superb/hubert-large-superb-er](https://huggingface.co/superb/hubert-large-superb-er)

---

## 🧑💻 Author

**Momin Mohammed Arfat**  
Full Stack / Python Developer  
⭐ GitHub: [@mdarfatwork](https://github.com/mdarfatwork)
