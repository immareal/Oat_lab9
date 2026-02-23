import librosa
import numpy as np
import soundfile as sf

y, sr = librosa.load('sapagetti.mp3')

def peak_dbfs(signal):
    peak = np.max(np.abs(signal))
    dbfs = 20 * np.log10(peak)
    return peak, dbfs

peak_before, db_before = peak_dbfs(y)

print("ก่อน Normalize")
print(f"Peak (linear): {peak_before:.6f}")
print(f"Peak (dBFS): {db_before:.2f} dBFS")

target_peak = 10 ** (-1 / 20) 
gain = target_peak / peak_before
y_norm = y * gain

peak_after, db_after = peak_dbfs(y_norm)

print("หลัง Normalize")
print(f"Peak (linear): {peak_after:.6f}")
print(f"Peak (dBFS): {db_after:.2f} dBFS")

