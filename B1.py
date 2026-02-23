from PIL import Image
import numpy as np

img = Image.open("image1.jpg")

img_array = np.array(img)

gray_array = img_array.mean(axis=2).astype('uint8')

gray_img = Image.fromarray(gray_array)

gray_img.save("gray_mean.jpg")
gray_img.show()

mean = np.mean(img_array)
std = np.std(img_array)

print('ค่าเฉี่ยเท่ากับ :', mean, 'ส่วนเบี่ยงเบนมาตรฐานเท่ากับ :',std)