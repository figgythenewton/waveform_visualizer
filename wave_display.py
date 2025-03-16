import librosa as lb
import numpy as np

class WaveDisplay():
    def __init__(self, filename, sr=44100, t=0):
        self.waveform, self.sample_rate = lb.load(filename, sr=sr)
        self.t = t
    
    def update(self):
        self.t += 1
    
    def get_ft(self, **kwargs):
        self.ft_matrix = lb.stft(self.waveform, **kwargs)
        print(self.ft_matrix.shape)
    
    def get_ft_frame(self, x, y):
        current_ft_frame = self.ft_matrix[:, self.t]
        return list(zip(
            np.arange(x, step=x/current_ft_frame.shape[0]), 
            np.clip(np.abs(current_ft_frame*4), a_min=0, a_max=y)
            ))
    
    def get_ft_log_frame(self, x, y):
        current_ft_frame = self.ft_matrix[:, self.t]
        return list(zip(
            np.logspace(0, np.log10(x), num=x).astype(int), 
            np.clip(np.abs(current_ft_frame), a_min=0, a_max=y)
            ))