import cv2
import os
from PIL import Image

cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalcatface_extended.xml')
cat_face_cascade = cv2.CascadeClassifier(cascade_path)

cat_img = 'cat.jpg'
# cat_img = 'cat.webp'
image = cv2.imread(cat_img)

glasses = Image.open('glasses.png')
cat = Image.open(cat_img)

cat_face = cat_face_cascade.detectMultiScale(image)

print(cat_face)

for (x, y, width, height) in cat_face:
    # cv2.rectangle(image, (x,y), (x+width, y+height), (0,255,0), 3)
    cat.paste(glasses, (x + 5, int(y + height / 10)), glasses)
    cat.save("cat_with_glasses.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("Cat_with_glasses", cat_with_glasses)

cv2.waitKey()