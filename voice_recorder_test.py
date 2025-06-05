# voice_recorder_test.py
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import av
import numpy as np
import queue
import soundfile as sf
import os
import tempfile
import speech_recognition as sr

st.title("🎤 Microphone Recorder Test")

audio_queue = queue.Queue()

class AudioProcessor:
    def __init__(self) -> None:
        self.recorded = []

    def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
        pcm = frame.to_ndarray()
        audio_queue.put(pcm)
        return frame

ctx = webrtc_streamer(
    key="mic-test",
    mode=WebRtcMode.SENDRECV,
    audio_receiver_size=256,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": False, "audio": True},
    audio_processor_factory=AudioProcessor,
    sendback_audio=False,
)

if st.button("🎧 Transcribe"):
    st.info("Processing audio...")
    audio_data = []
    while not audio_queue.empty():
        audio_data.append(audio_queue.get())

    if audio_data:
        audio_array = np.concatenate(audio_data, axis=1).flatten().astype(np.float32)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            sf.write(f.name, audio_array, samplerate=48000)
            f.flush()
            recognizer = sr.Recognizer()
            with sr.AudioFile(f.name) as source:
                audio = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio)
                    st.success("Transcription:")
                    st.write(text)
                except sr.UnknownValueError:
                    st.error("Speech Recognition could not understand audio.")
                except sr.RequestError as e:
                    st.error(f"Could not request results; {e}")
        os.remove(f.name)
    else:
        st.warning("No audio captured.")
