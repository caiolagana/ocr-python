#following https://towardsdatascience.com/build-optical-character-recognition-ocr-in-python-28d1c7b77da3

from PIL import Image
import pytesseract
import numpy as np
from pytesseract import Output
import cv2

filename = 'test_image.jpeg'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)

image = cv2.imread(filename)
results = pytesseract.image_to_data(image, output_type=Output.DICT)

for i in range(0, len(results[“text”])):
    x = results[“left”][i]
    y = results[“top”][i]
    
    w = results[“width”][i]
    h = results[“height”][i]
    text = results[“text”][i]
    conf = int(results[“conf”][i])
    if conf > 70:
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)
cv2.imshow(image)