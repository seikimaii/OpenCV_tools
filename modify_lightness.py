#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 02:58:30 2021

@author: seikimaii
"""
import cv2
import numpy as np
import sys
def modify_lightness(img,lightness=0,saturation=0):
    
    nimg = img.astype(np.float32)
    nimg = nimg / 255.0
    
    hls_img = cv2.cvtColor(nimg,cv2.COLOR_BGR2HLS)
    
    hls_img[:,:,1] *= (1 + lightness/100.0)
    hls_img[:,:,1][hls_img[:,:,1]>1] = 1
    
    hls_img[:,:,2] *= (1 + saturation/100.0)
    hls_img[:,:,2][hls_img[:,:,2]>1] = 1
    
    mod_img = cv2.cvtColor(hls_img,cv2.COLOR_HLS2BGR)
    mod_img = (mod_img*255).astype(np.uint8)
    
    return mod_img

if __name__ == '__main__':
    
    img = cv2.imread(input('iamge path :'))
    if img is None:
        sys.exit('No image!')
    lightness = float(input('lightness factor ='))
    saturation = float(input('saturation factor ='))
    
    mod_img = modify_lightness(img,lightness,saturation)
    
    cv2.imshow('origin',img)
    cv2.imshow('mod_img',mod_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    