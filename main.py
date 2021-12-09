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
        img = Image.open(filename)
        image_list.append(img)

    for x in image_list:
        new_image = transforms.adjust_brightness(x, 1.5)
        new_image = transforms.adjust_contrast(new_image, 10)
        new_image = transforms.adjust_saturation(new_image, 0.2)
        if not os.path.exists('images'):
            os.mkdir('images')
        new_image.save("images/new_image{0}.jpg".format(image_list.index(x)+1))

if __name__ == "__main__":
    main()

