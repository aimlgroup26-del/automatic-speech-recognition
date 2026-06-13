import os


def validate_audio_file(path: str) -> bool:
    supported = {".wav", ".mp3", ".m4a", ".flac"}
    return os.path.isfile(path) and os.path.splitext(path)[1].lower() in supported
