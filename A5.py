import os

folder_path = "d:/udom/lab_9"

files = os.listdir(folder_path)

keyword = input('กรอกคำค้นหา : ')

matched_files = [f for f in files if keyword in f]

print("ไฟล์ที่เจอ:", matched_files )
