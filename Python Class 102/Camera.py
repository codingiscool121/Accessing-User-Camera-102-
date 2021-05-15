import cv2

def takepicture():
    videocaptureobject = cv2.VideoCapture(0)
    result=True
    while(result):
        on,frame=videocaptureobject.read()
        cv2.imwrite("stalker.jpg", frame)
        result=False 
    
    videocaptureobject.release()
    cv2.destroyAllWindows()

takepicture()