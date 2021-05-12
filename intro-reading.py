# read images, video, webcam
import cv2

# IMAGE
img = cv2.imread("images/download-8.jpg")
cv2.imshow("First Image", img)
cv2.waitKey(60*1000) # infinite delay or # in mili seconds

# VIDEO
cap = cv2.VideoCapture("videos/Cat-Falling-Asleep.mp4")
while True:
    success, img=cap.read() # success is boolean t/f for if cap successful
    cv2.imshow("First Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'): # if q key is pressed it quits
        break


# WEBCAM
web = cv2.VideoCapture(0) # 0 = default webcam
web.set(3, 640) # 3=width
web.set(4, 480) # 4=height
web.set(10, 100) # 10=brightness
while True:
    success, img=web.read() # success is boolean t/f for if cap successful
    cv2.imshow("First Webcam", img)
    if cv2.waitKey(1) & 0xFF==ord('q'): # if q key is pressed it quits
        break

web.release()
cv2.destroyAllWindows()