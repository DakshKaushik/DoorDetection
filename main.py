import cv2 as cv
import numpy as np
from selenium import webdriver
#import os
import subprocess
capture=cv.VideoCapture(1)

k=0
while(k<50):
     check,first_frame=capture.read()
     k+=1

def img_preprocessing(frame):
    resized_img=frame[450:600,800:1000]
    gray=cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
    #blur=cv.GaussianBlur(gray,(9,9),0)
    return gray

first=img_preprocessing(first_frame)

while(True):
    isTrue,frame=capture.read()
    
    frame_rec=img_preprocessing(frame)
    cv.imshow('video',frame_rec)
       
    frame_diff= cv.absdiff(frame_rec, first)
    _, thresh = cv.threshold(frame_diff, 25, 255, cv.THRESH_BINARY)

    white_pixel_count = np.sum(thresh == 255)
    if(white_pixel_count >2000):
        #os.system("pkill firefox") 
        subprocess.run(["pkill", "firefox"]) #subprocess is faster than os
        break
    #not needed now
    # contours, _ = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # for contour in contours:
    #         if cv.contourArea(contour) < 1000: 
    #             continue
    #         (x, y, w, h) = cv.boundingRect(contour)
    #         cv.rectangle(frame_rec, (x, y), (x + w, y + h), (0, 255, 0), 2)    
    # cv.imshow('Change Detection', frame_rec)
    
    if cv.waitKey(20)&0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()
