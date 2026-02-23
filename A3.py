import re

text = input('กรอกข้อความ : ')
sentences = re.split(r'[.!?]+', text)
l = len(sentences)

results = []
k = []

for i in sentences:
    words = i.split()
    results.append((i, len(words)))
    k.append(len(words))

max_result = max(results, key=lambda x: x[1])
avg = sum(k)
print('ประโยคที่เยอะที่สุดคือ ',max_result)
print(f'ค่าเฉลี่ย = {avg/(l-1)}')
