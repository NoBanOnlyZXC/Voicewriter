from vosk import Model, KaldiRecognizer
import pyaudio

model = Model('./voice/vosk')
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

def speech():
    stream.start_stream()

    data = stream.read(4096, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()[14:-3]
        return text