import numpy as np
import importlib
from cv2 import cv2
from matplotlib import pyplot as plt

print(cv2.__version__)

img = cv2.imread('test_image.jpg')
img2 = img[..., ::-1]
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img2)
# plt.xticks([]), plt.yticks([])
plt.show()
