import librosa
import numpy as np

def load_audio_file(filename):
    y, sr = librosa.load(filename)
    return y, sr
