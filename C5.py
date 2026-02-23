import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

y, sr = librosa.load("sapagetti.mp3", sr=None)

D = librosa.stft(y, n_fft=2048, hop_length=512)

S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

plt.figure(figsize=(10, 5))
librosa.display.specshow(S_db,
                         sr=sr,
                         hop_length=512,
                         x_axis='time',
                         y_axis='hz')

plt.colorbar(format='%+2.0f dB')
plt.title("Spectrogram")
plt.tight_layout()
plt.show()

