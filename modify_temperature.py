#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 01:51:53 2021

@author: seikimaii
"""

import cv2
import numpy as np


def modify_temperature(img,mode='default',degree=0):
    
    # img = img.astype(np.float32)
    b = img[:,:,0]
    g = img[:,:,1]
    r = img[:,:,2]
    bAve = np.mean(b)
    gAve = np.mean(g)
    rAve = np.mean(r)
    
    if mode == 'default':
        
        bAve += degree
        gAve += degree
        rAve += degree
        
    elif mode == 'cold':
        
        gAve += degree
        rAve += degree
        
    elif mode == 'warm':
        
        bAve += degree
        gAve += degree
        
        
    AllAve = (bAve + gAve + rAve) // 3
    bCoef = AllAve / bAve
    gCoef = AllAve / gAve
    rCoef = AllAve / rAve
    b = np.floor(b * bCoef)
    g = np.floor(g * gCoef)
    r = np.floor(r * rCoef)
    
    imgb = b
    imgb[imgb > 255] = 255
    imgg = g
    imgg[imgg > 255] = 255
    imgr = r
    imgr[imgr > 255] = 255
    de_img = np.dstack((imgb,imgg,imgr)).astype(np.uint8)
    return de_img

if __name__ == '__main__' :
    img = cv2.imread('drum_fan.jpg')
    mode = input('mode:')
    degree = int(input('degree:'))
    style_img = modify_temperature(img,mode,degree)
    cv2.imshow('ori',img)
    cv2.imshow('style',style_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)