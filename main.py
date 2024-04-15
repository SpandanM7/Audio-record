import pyaudio
import wave

def record_audio(output_file, duration=5, sample_rate=44100, channels=2, format=pyaudio.paInt16):
    audio = pyaudio.PyAudio()

    # Open stream for recording
    stream = audio.open(
        format=format,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=1024
    )

    print("Recording...")

    frames = []
    for _ in range(int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Recording finished.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved to {output_file}")

if __name__ == "__main__":
    output_file = "recorded_audio.wav"
    duration = int(input("Enter duration of recording in seconds:"))  # seconds
    record_audio(output_file, duration)
