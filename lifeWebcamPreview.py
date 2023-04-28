# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:09:33 2021

@author: birkudo
"""
import numpy as np
import cv2
import platform

DEVICE_ID = 0 # change here, to open your preferred webcam 

def main():
    if platform.system() == 'Windows':
        videoBackend = cv2.CAP_DSHOW
    else:
        videoBackend = cv2.CAP_ANY
    cap = cv2.VideoCapture(DEVICE_ID, videoBackend);
    
    if not cap.isOpened():
        print('ERROR: could not open webcam');
        
    while(True):
        ret, frame = cap.read();
        if not ret:
            print('ERROR: could not read data from webcam')
            break;
        
        cv2.imshow("Press 'q' to quit.", frame)
        ch = cv2.waitKey(20);
        if ch==ord('q'):
            break;
        if ch==ord('0'):
            cap.set(cv2.CAP_PROP_SETTINGS,0);

    cap.release();
    cv2.destroyAllWindows();
    
    
if __name__ == "__main__":
    main();