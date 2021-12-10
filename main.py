import numpy as np
import torch
import torchvision.transforms.functional as transforms
import glob
import os
from PIL import Image
import PIL.ImageOps

def main():
    image_list = []
    for filename in glob.glob("coni/*.jpg"):
        image_list.append(filename)

    if not os.path.exists('images'):
        os.mkdir('images')

    for image in image_list:
        img = Image.open(image)
        new_image = transforms.adjust_brightness(img, 1.5)
        new_image = transforms.adjust_contrast(new_image, 10)
        new_image = transforms.adjust_saturation(new_image, 0.2)

        new_image.save("images/new_image{0}.jpg".format(image_list.index(image)+1), quality = 75)

if __name__ == "__main__":
    main()



