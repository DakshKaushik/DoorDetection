import cv2 as cv
capture=cv.VideoCapture(1)

k=0
while(k<5):
     check,first_frame=capture.read()
     k+=1

def img_preprocessing(frame):
    resized_img=frame[400:600,800:1100]
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
    contours, _ = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
            if cv.contourArea(contour) < 900: 
                continue
            (x, y, w, h) = cv.boundingRect(contour)
            cv.rectangle(frame_rec, (x, y), (x + w, y + h), (0, 255, 0), 2)    
    cv.imshow('Change Detection', frame_rec)
    
    if cv.waitKey(20)&0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()
