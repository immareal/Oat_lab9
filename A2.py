import re

text = input('กรอกข้อความ : ')
text1 = text
words = text1.lower()
de = words.replace(" ", "")
clean = re.sub(r'[^a-zA-Z0-9ก-๙\s]', '', de)

print(f'ก่อน : {text}')
print(f'หลัง : {clean}')