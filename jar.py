
import sounddevice as sd

MICROPHONE_ID = 1

print("JARVIS microphone test started")
print("SPEACK ANYTHING FOR 5 SECONDS...")

recording = sd.rec(
    int(5 * 16000),
    samplerate=16000,
    channels=1,
    dtype="int16",
    device=MICROPHONE_ID
)

sd.wait()

print("Recording completed!")
print("Recorded audio samples:", len(recording))
