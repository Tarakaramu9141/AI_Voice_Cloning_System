# Enhanced AI Voice Cloning System
 
📌 A Streamlit-based application for high-quality voice cloning using YourTTS (Text-to-Speech)

## 📑 Table of Contents
1. Features
2. How it works
3. Installation and Setup
4. Usage Guide
5. Alternatives for Improvement
6. Limitations
7. Future Enhancements
8. License

## ✨ Features
1. High-Quality Voice Cloning
- Uses YourTTs (a multilingual TTS model) for realistic voice synthesis.
- Supports voice cloning from short audio samples (10-30 sec recommended).
2. Audio Preprocessing for Better Accuracy.
- Auto-normalization (prevents clipping and distortion).
- Resampling to 22.05kHz(optimal for TTS models).
- Stereo-to-Mono conversion (improves model compatibility).
3. Customizable Speech Generation
- Temperature Control (adjusts voice stability vs. variation).
- Speed Adjustment (faster/slower speech generation).
- Language Selection (English, Spanish, French, German).
4. User-Friendly Interface
- Streamlit-based UI (simple & interactive).
- Real-time audio playback (listen before downloading).
- Download generated audio (WAV format).
5. CPU-Compatible
- Optimized for CPU usage (no GPU required).

## How it works
1. Upload Audio Sample (WAV/MP3, 10-30 sec recommended).
2. Preprocessing (normalization, resampling, mono conversion).
3. Enter Text (what you want the cloned voice to say).
4. Generate & Download (customizable speed, temperature, language).


## ⚙️ Installation & Setup
Pre-requisites
- python 3.8+
- pip 

Steps
1. Clone the repository
git clone[ https://github.com/tarakaramu9141/voice-cloning-app.git](https://github.com/Tarakaramu9141/AI_Voice_Cloning_System.git)
2. Install dependencies
pip install -re requirements.txt
3. Run the Streamlit app
streamlit run app.py
4. Open in browser
- The app will run at http://localhost:8501.

## 📖 Usage Guide
1. Upload Audio
- Use a clean recording (minimal background noise).
- 10-30 seconds of speech works best.
2. Adjust Settings(Optional)
- Temperature: Lower = more stable, Higher = more expressive.
- Speed: 0.5x (slow) to 1.5x (fast).
- Language: English (en) recommended for best results.
3. Enter Text & Generate
- Type the text you want the AI to speak.
- Click "Generate Cloned Voice".
4. Download Audio
- Play the output and download if satisfied.

## Alternatives for Improvement
1. Better TTS Models

Model                 	             Pros              	                   Cons
Coqui TTS (YourTTS) ||	Good for cloning, multilingual	CPU-friendly ||but limited expressiveness
Tortoise TTS	       || Extremely realistic clones	Slow             || requires GPU
ElevenLabs	         || Best commercial quality	                    ||API-based (paid)
VITS (V2)	          || High-quality open-source	                   ||Needs fine-tuning

2. Enhanced Preprocessing
- Noise Reduction (using RNNoise or Adobe Audition).
- Voice Activity Detection (VAD) (remove silent parts).
- Speaker Diarization (isolate single speaker if multiple voices exist).
 
3. Post-Preprocessing for Naturalness
- Pitch Correction (match original speaker’s tone).
- Prosody Adjustment (improve speech rhythm).
- WaveNet/Griffin-Lim vocoders (better audio quality).

4. Deployment Improvements
- GPU Acceleration (for faster inference).
- API-based TTS (ElevenLabs, PlayHT for better quality).
- Edge Deployment (ONNX/TensorRT optimization).

## ⚠️ Limitations
- Short samples (<3 sec) reduce quality.
- Background noise affects cloning accuracy.
- Non-English voices may sound less natural.
- CPU mode is slower than GPU.

## 🚀 Future Enhancements
✅ Real-time voice cloning (microphone input).
✅ Emotion control (happy, sad, angry tones).
✅ Batch processing (generate multiple sentences at once).
✅ Fine-tuning option (improve specific voice accuracy).

## 📜 License
MIT-License

## 🔗 References
- Coqui TTS GitHub[https://github.com/coqui-ai/TTS]
- Streamlit Docs[https://docs.streamlit.io/]

## 🎯 Conclusion
This app provides decent-quality voice cloning with CPU support, but for professiona use, consider:
🔹 Tortoise TTS (GPU needed).
🔹 ElevenLabs API (best quality, paid).
🔹 Custom fine-tuning (for specific voices).
