import cv2

import numpy as np
fb_cas = cv2.CascadeClassifier('/home/hp/PycharmProjects/tryOndetector/haarcascades/haarcascade_lowerbody.xml')
haar_upper_body_cascade = cv2.CascadeClassifier("/home/hp/PycharmProjects/tryOndetector/haarcascades/haarcascade_upperbody.xml")
face_cascade=cv2.CascadeClassifier("/home/hp/PycharmProjects/tryOndetector/haarcascades/haarcascade_frontalface_default.xml")
blazer = cv2.imread("/home/hp/Downloads/dataset/jackets/Blazers/maleBlazers/Blazers4.png", cv2.IMREAD_UNCHANGED)
bgr = blazer[:,:,:3]
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

# Some sort of processing...
fw=0

#bgr = cv2.cvtColor(bgr, cv2.COLOR_GRAY2BGR)
alpha = blazer[:,:,3] # Channel 3
result = np.dstack([bgr, alpha])
resultblazer = cv2.resize(result,(300,450))

#jeans
jeans = cv2.imread("/home/hp/Downloads/image.png", cv2.IMREAD_UNCHANGED)
bgr = jeans[:,:,:3]
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

# Some sort of processing...
fw=0

#bgr = cv2.cvtColor(bgr, cv2.COLOR_GRAY2BGR)
alpha = jeans[:,:,3] # Channel 3
result = np.dstack([bgr, alpha])
resultjeans = cv2.resize(result,(300,450))
#cv2.imshow("dress",jeans)

#cv2.imshow("dress",dress)
girl = cv2.imread("/home/hp/Downloads/AS.jpg")
girl=cv2.resize(girl,(289,385))
gray = cv2.cvtColor(girl, cv2.COLOR_BGR2GRAY)
face =face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=4,

)
H=0
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
found,w = hog.detectMultiScale(girl, winStride=(8,8), padding=(32,32), scale=1.05)
for (mx,my,mw,mh) in face:
   # cv2.rectangle(girl, (mx, my), (mx + mw, my + mh), (0, 255, 0), 6)
    H=mh
    Fw=mw
lower_body = fb_cas.detectMultiScale(
    gray,
    scaleFactor=1.01,
    minNeighbors=5,
    minSize=(1, 1),  # Min size for valid detection, changes according to video size or body size in the video.
    flags=cv2.CASCADE_SCALE_IMAGE
)
for (x,y,w,h) in lower_body:
    #cv2.rectangle(girl, (x, y), (x + w, y + h), (0, 255, 0), 6)
    girl = cv2.cvtColor(girl, cv2.COLOR_BGR2BGRA)
    dress = cv2.resize(resultjeans, (w-10, h))
    # girl=cv2.resize(girl,(fw,girl.shape[0]))
    print(fw)
    w, h, c = dress.shape
    for i in range(0, w):
        for j in range(0, h):

            if dress[i, j][3] != 0:
                girl[y + i, x + j] = dress[i, j]

for x, y, w, h in found:
    # the HOG detector returns slightly larger rectangles than the real objes.
    # so we slightly shrink the rectangles to get a nicer output.
    h=int(h/2.3)
    pad_w, pad_h = int(0.15 * w), int(0.05 * h)
    #cv2.rectangle(girl, (x, y+H), (x + w, y + h), (0, 255, 0), 10)
    girl = cv2.cvtColor(girl, cv2.COLOR_BGR2BGRA)
    dress = cv2.resize(resultblazer, (w + Fw - 70, h ))
    # girl=cv2.resize(girl,(fw,girl.shape[0]))

    w, h, c = dress.shape
    for i in range(0, w):
        for j in range(0, h):

            if dress[i, j][3] != 0:
                girl[y + i + 40, x + j - Fw + 67] = dress[i, j]

cv2.imshow("girl", girl)
cv2.waitKey(0)