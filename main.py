import numpy as np
import torch
from PIL import Image
import PIL.ImageOps

image = Image.open("./cone71_frame39.jpg")
inverted = PIL.ImageOps.invert(image)
inverted.save("conoinverito.png")



