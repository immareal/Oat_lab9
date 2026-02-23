from PIL import Image

img = Image.open("image1.jpg")

width, height = img.size

i = width/height

x = int(input('กรอกความกว้าง : '))
y =  x/i

resized = img.resize((int(x), int(y)))

resized.save("resized.jpg")
resized.show()

print('ก่อน : ',img.size)
print('หลัง : ',resized.size)