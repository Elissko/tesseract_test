import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path = r'D:\coding\tesseract_filter\screens'
custom_config = r'--oem 1 --psm 1'
folder_images = 'screens'

images = []

if not os.path.isdir('filtered_img'):
     os.mkdir('filtered_img')

for root, dirs, files in os.walk(path):
    for file in files:
        images.append(os.path.join(root, file))


for image in images:
    img = Image.open(os.path.join(folder_images, image))
    text = pytesseract.image_to_string(img, config=custom_config)
    if len(text.strip()) == 0:
        os.replace(image, 'filtered_img/' + os.path.basename(image))