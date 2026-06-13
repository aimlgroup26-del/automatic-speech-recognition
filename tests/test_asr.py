from src.utils import validate_audio_file


def test_validate_audio_file_invalid():
    assert validate_audio_file("nonexistent.wav") is False


def test_validate_audio_unsupported_format():
    assert validate_audio_file("file.txt") is False
