import librosa
import soundfile as sf

y, sr = librosa.load('sapagetti.mp3', sr=None)

duration_before = librosa.get_duration(y=y, sr=sr)

y_trimmed, index = librosa.effects.trim(y, top_db=30)

sf.write("output_trimmed.wav",
         y_trimmed.T if y_trimmed.ndim==2 else y_trimmed,
         sr)

y_after, sr_after = librosa.load("output_trimmed.wav", sr=None)

duration_after = librosa.get_duration(y=y_after, sr=sr_after)

print("ระยะเวลาก่อน :", duration_before)
print("ระยะเวลาหลัง :", duration_after)
