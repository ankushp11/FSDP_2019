# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:08:53 2019

@author: user
"""
from PIL import Image
import os
img=Image.open("sample.jpg")
img_gray=img.convert('L')
img_gray.save("sample1.jpg")
img1=img_gray.transpose(Image.ROTATE_90)
img1.save("sample1.jpg")
crop_im = img1.crop(box=(20, 340, 160, 204))
crop_im.save("sample1.jpg")
crop_im.thumbnail((75, 75))
print(crop_im.width, crop_im.height)
crop_im.save('sample1.jpg')