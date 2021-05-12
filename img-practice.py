import cv2
import numpy as np

# img functions
img = cv2.imread("images/orange-cat.jpg")
kernel = np.ones((5,5),np.uint8)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (7,7), 0) # must be odd numbers
imgEdges = cv2.Canny(img, 150, 200) # two threshold values
imgDialation = cv2.dilate(imgEdges, kernel, iterations=1)
imgErosion = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Grey Image", imgGrey)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Edges Image", imgEdges)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Erosion Image", imgErosion)
cv2.waitKey(0)

# resizing
print(img.shape) # (408, 612, 3) height,width,bgr
imgResize = cv2.resize(img, (400,250)) #width,height
print(imgResize.shape)

# cropping
imgCropped = img[0:200][0:200]

cv2.imshow("Image", img)
cv2.imshow("Resized", imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)

# shapes and text
img = np.zeros((512,512,3)) 
print(img.shape)

# color whole image vs. part of image
img[:]=255,0,0
img[300:400] =255,255,255

# shapes
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.rectangle(img,(0,0),(50,50),(0,0,255),2)
cv2.circle(img,(400,100),30,(255,255,0),5)

# text
cv2.putText(img,"HELLO WORLD",(50,350),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)

cv2.imshow("Image",img)
cv2.waitKey(0)
