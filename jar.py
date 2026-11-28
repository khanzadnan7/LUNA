import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

#Configuration
MODEL_PATH = "vosk-model-small-en-us-0.15"
MICROPHONE_ID = 1
SAMPLE_RATE = 16000

# Audio queue
audio_queue = queue.Queue()

# Microphone callback
def audio_callback(indata, frames, time, status):
    if status:
        print("Audio status:", status)

    audio_queue.put(bytes(indata))


# Load speech recognition model
print("Loading LUNA...")

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

print("LUNA is ready!")
print("StaRt speaking. Press Ctrl+C to stop.\n")


# Start microphone
try:
    with sd.RawInputStream(
        device=MICROPHONE_ID,
        samplerate=SAMPLE_RATE,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=audio_callback
    ):

        while True:
            audio_data = audio_queue.get()

            if recognizer.AcceptWaveform(audio_data):
                result = json.loads(recognizer.Result())

                recognized_text = result.get("text", "").strip()

                if recognized_text:
                    if recognized_text.lower()== "stop luna":
                        print("LUNA STOPPED LISTENING.....")
                        break
                    print("You:", recognized_text)



except KeyboardInterrupt:
    print("\nLUNA stopped listening.")
