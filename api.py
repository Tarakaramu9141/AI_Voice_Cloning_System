import streamlit as st
import os
from TTS.api import TTS
import warnings
import soundfile as sf
import numpy as np
from scipy import signal

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# Initialize directories
OUTPUT_DIR = "output"
SAMPLE_DIR = "sample_audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SAMPLE_DIR, exist_ok=True)

# Audio preprocessing function
def preprocess_audio(input_path, output_path, target_sr=22050):
    """Normalize and resample audio for better TTS performance"""
    try:
        # Read audio file
        audio, sr = sf.read(input_path)
        
        # Convert stereo to mono if needed
        if len(audio.shape) > 1:
            audio = np.mean(audio, axis=1)
            
        # Normalize audio to -1dB to prevent clipping
        peak = np.max(np.abs(audio))
        if peak > 0:
            audio = audio * (0.9 / peak)
            
        # Resample if needed
        if sr != target_sr:
            audio = signal.resample_poly(audio, target_sr, sr)
            
        # Write processed audio
        sf.write(output_path, audio, target_sr)
        return True
    except Exception as e:
        st.error(f"Audio processing failed: {str(e)}")
        return False

# Load the TTS model with more configuration options
@st.cache_resource
def load_tts_model():
    # Using YourTTS with more configuration for better quality
    model_name = "tts_models/multilingual/multi-dataset/your_tts"
    tts = TTS(
        model_name=model_name,
        progress_bar=False,
        gpu=False,  # Explicitly set to CPU
    )
    return tts

# Main Streamlit app
def main():
    st.title("Enhanced AI Voice Cloning System")
    st.write("""
    Upload a clear audio sample (10-30 seconds of speech) to clone a voice and generate speech from text. 
    For best results, use a high-quality recording with minimal background noise.
    """)

    # Sidebar with advanced options
    with st.sidebar:
        st.header("Advanced Settings")
        temperature = st.slider("Voice Variation (Temperature)", 0.1, 1.0, 0.7, 
                              help="Lower values make voice more stable, higher values more varied")
        speed = st.slider("Speech Speed", 0.5, 1.5, 1.0, 
                         help="Adjust the speed of generated speech")
        language = st.selectbox("Language", ["en", "es", "fr", "de"], 
                               help="Select output language (English works best)")

    # Load the TTS model
    tts = load_tts_model()

    # File uploader for voice sample
    uploaded_file = st.file_uploader("Upload a clear audio sample (WAV format, 10-30 seconds)", 
                                   type=["wav", "mp3"])
    
    if uploaded_file is not None:
        # Save the uploaded file temporarily
        sample_path = os.path.join(SAMPLE_DIR, "uploaded_sample.wav")
        with open(sample_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Preprocess the audio
        processed_path = os.path.join(SAMPLE_DIR, "processed_sample.wav")
        if preprocess_audio(sample_path, processed_path):
            st.audio(processed_path, format="audio/wav")
            st.success("Audio processed successfully!")
            
            # Show audio duration
            audio_info = sf.SoundFile(processed_path)
            duration = len(audio_info) / audio_info.samplerate
            st.info(f"Audio duration: {duration:.2f} seconds")
            
            if duration < 3:
                st.warning("For best results, use a longer audio sample (10-30 seconds)")
            elif duration > 60:
                st.warning("Very long audio may reduce quality. Consider using a 10-30 second sample.")

            # Text input for speech generation
            text_input = st.text_area("Enter the text you want the cloned voice to say:", 
                                     "Hello, this is an improved voice cloning system that produces more accurate results.")
            
            if st.button("Generate Cloned Voice"):
                if text_input.strip() == "":
                    st.error("Please enter some text to generate speech.")
                else:
                    with st.spinner("Generating high-quality audio... This may take a moment on CPU."):
                        # Generate the output file with more parameters
                        output_path = os.path.join(OUTPUT_DIR, "cloned_output.wav")
                        tts.tts_to_file(
                            text=text_input,
                            speaker_wav=processed_path,
                            language=language,
                            file_path=output_path,
                            temperature=temperature,
                            speed=speed,
                            emotion="Neutral",  # More stable output
                        )
                    
                    # Display the generated audio
                    st.success("High-quality voice cloning complete!")
                    st.audio(output_path, format="audio/wav")
                    
                    # Provide download link
                    with open(output_path, "rb") as file:
                        st.download_button(
                            label="Download Generated Audio",
                            data=file,
                            file_name="cloned_output.wav",
                            mime="audio/wav"
                        )

    else:
        st.info("Please upload an audio file to start cloning. For best results:")
        st.markdown("""
        - Use a clean recording (minimal background noise)
        - 10-30 seconds of continuous speech
        - WAV format recommended (MP3 also supported)
        - Single speaker (no overlapping voices)
        """)

if __name__ == "__main__":
    main()