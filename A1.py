from collections import Counter
import re


text = input('กรอกข้อความ : ')

clean = re.sub(r'[^a-zA-Z0-9ก-๙\s]', '', text)
words = clean.lower().split()
word_count = Counter(words)
top10 = word_count.most_common(10)

for word, count in top10:
    print(f'{word} : {count}')

