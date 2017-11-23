import cv2
import numpy as np

cap = cv2.VideoCapture(1)

r, aa = cap.read()

x = np.zeros((aa.shape[0] + 100, aa.shape[1] + 100, 3))

for i in range(0, aa.shape[0]):
    print(i)
x[0:aa.shape[0], 0:aa.shape[1], 0:3] = aa[0:aa.shape[0], 0:aa.shape[1], 0:3]/255.0

cv2.imshow("aa", aa)
cv2.imshow("x", x)


cv2.waitKey(0)