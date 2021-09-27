#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 03:44:21 2021

@author: seikimaii
"""
import numpy as np
import cv2

def show_img(name,img):
    cv2.imshow(name,img)
    
def modify_intensity(img):
    origin_img = img
    print("origin picture:")
    show_img('origin',origin_img)
    
    #先做位元深度轉換，不然平方會爆掉
    origin_img = origin_img.astype(np.float32)
    
    maxIntensity = 255.0 # depends on dtype of image data

    
    # Increase intensity 
    increase_img = ((maxIntensity*origin_img)**0.5)
    increase_img = np.array(increase_img, dtype=np.uint8)
    print("Increase intensity :")
    show_img('increase',increase_img)

    # Decrease intensity  
    decrease_img = origin_img**2/maxIntensity#(maxIntensity/phi)*(origin_img/(maxIntensity/theta))**2
    decrease_img = np.array(decrease_img, dtype=np.uint8)
    print("Decrease intensity :")
    show_img('decrease',decrease_img)
    
if __name__ == '__main__':
    img = cv2.imread('CV_1/hunter.jpg')
    modify_intensity(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)