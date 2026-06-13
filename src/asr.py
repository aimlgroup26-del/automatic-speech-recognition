import whisper


def transcribe(audio_path: str, model_name: str = "base") -> str:
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result["text"]
