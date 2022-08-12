import os
import cv2
import numpy as np

dirs = ['ants_1', 'bees']
pixels = []
labels = []

for i, d in enumerate(dirs):
    #print(i , d)
    files = os.listdir('../data/' + d)

    for f in files :
        img = cv2.imread('../data/' + d + '/' + f, 0)
        img = cv2.resize(img, (128, 128))
        img = np.array(img).flatten().tolist()
        pixels.append(img)

        labels.append(i)

print(labels)

