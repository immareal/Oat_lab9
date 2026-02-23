import librosa

y, sr = librosa.load("sapagetti.mp3")

print("ระยะเวลา : ", librosa.get_duration(y=y, sr=sr))
print("Sample Rate : ", sr)
if y.ndim == 1:
    print("จำนวนช่องสัญญาณเป็น Mono")
else:
    print("จำนวนช่องสัญญาณเป็น Stereo")
