import pytest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from audex import menu, source_file, text_to_audio

def test_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert menu() == '1'
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert menu() == '2'
    monkeypatch.setattr('builtins.input', lambda _: '3')
    assert menu() == '3'

def test_source_file():
    with pytest.raises(FileNotFoundError):
        source_file("invalid.txt")
        source_file("incorrect.txt")

def test_text_audio():
    with pytest.raises(FileNotFoundError):
        text_to_audio("invalid.txt")
        text_to_audio("incorrect.txt")

