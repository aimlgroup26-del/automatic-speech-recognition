from asr import transcribe


def main():
    audio_file = "sample.wav"
    result = transcribe(audio_file)
    print(f"Transcription: {result}")


if __name__ == "__main__":
    main()
