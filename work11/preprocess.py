from __future__ import division
import numpy as np
import cv2
import glob
import sys
import os

def color_transfer(source1):
    source = cv2.imread("SOB_B_A-14-22549G-40-035.png")
    target = cv2.cvtColor(source1, cv2.COLOR_BGR2LAB).astype("float32")
    source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")

    (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
    (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)

    (l, a, b) = cv2.split(target)
    l -= lMeanTar
    a -= aMeanTar
    b -= bMeanTar

    l = (lStdSrc / lStdTar) * l
    a = (aStdSrc / aStdTar) * a
    b = (bStdSrc / bStdTar) * b

    l += lMeanSrc
    a += aMeanSrc
    b += bMeanSrc

    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)


    transfer = cv2.merge([l, a, b])
    transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)
    return transfer

def image_stats(image):

    (l, a, b) = cv2.split(image)
    (lMean, lStd) = (l.mean(), l.std())
    (aMean, aStd) = (a.mean(), a.std())
    (bMean, bStd) = (b.mean(), b.std())

    return (lMean, lStd, aMean, aStd, bMean, bStd)

if __name__=='__main__':
	for ii in ['100X','200X','400X']:
		for jj in ['fold1','fold2','fold3','fold4','fold5']:
			path="./"+jj+"/*/"+ii+"/*.png"
			print path
			images = glob.glob(path)
			print images
			for image in images:
				source = cv2.imread(image)
				transfer = color_transfer(source)
				cv2.imwrite('preprocess' + image.replace("png", "jpg")[1:],transfer)
				print(image,' Done.')
