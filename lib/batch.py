# written by longriyao
#coding: utf-8

import cv2
import numpy as np
def get_batch(batch_paths,has_label):
    blobs = {}
    for batch in batch_paths:



    blobs['gray_image'] = gray_image
    blobs['color_image'] = color_image
    if has_label:
        label = np.zeros(len(batch_paths)*2,dtype=np.float32)
        label[(len(batch_paths)-1):] = 1
        blobs['label'] = label
    return blobs

