import cv2
import glob
import time

'''
# grey scale = 0, as it is = 1
img_rd = cv2.imread("index.jpg",1)
print(type(img_rd))
print(img_rd)
print(img_rd.shape)
print(img_rd.ndim)

cv2.imshow("Galaxy",img_rd)
cv2.waitKey(5000)
cv2.destroyAllWindows()
'''
'''
images = glob.glob("sample-images\\*.jpg")
cnt=1
for image in images:
    print(image)
    img = cv2.imread(image,1)
    re = cv2.resize(img,(100,100))
    cv2.imshow("test",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resize_"+str(cnt)+".jpg",re)
    cnt=cnt+1

'''

#haarcascade xml files for fact recognition.

#Video Capture

video = cv2.VideoCapture(0)
a=1
while True:
    a=a+1
    return_value, image = video.read()
#    cv2.imwrite("myPic.jpg",image)
#    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#    time.sleep(3)
    cv2.imshow("show",image)
    key = cv2.waitKey(1)
    if (key==ord('q')):
        break
print("Frames captured:",a)
video.release()
cv2.destroyAllWindows()
