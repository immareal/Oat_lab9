import re

text = input('กรอกข้อความ : ')

keyword = ['ฟรี','ด่วน','คลิก','โปรโมชั่น','เงินคืน','รับทันที']

keyword1 = ['http','https']

pattern = r'(.)\1{4,}'

match = re.search(pattern, text)

point = 0

for k in keyword:
    if k in text:
        point += 2
        break   

for k in keyword1:
    if k in text:
        point += 3
        break

if match:
    point += 2

if point > 5 :
    print('สแปม')
elif point >2 :
    print('น่าสงสัย')
else:
    print('ปกติ')