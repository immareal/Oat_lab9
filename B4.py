from PIL import Image, ImageFilter

img = Image.open("image1.jpg")

x1 = int(input('ซ้าย : '))
y1 = int(input('บน : '))
x2 = int(input('ขวา : '))
y2 = int(input('ล่าง : '))

roi = img.crop((x1, y1, x2, y2))

blur_roi = roi.filter(ImageFilter.GaussianBlur(10))

img.paste(blur_roi, (x1, y1))

img.show()
img.save("blur_result.jpg")