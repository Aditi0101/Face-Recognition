import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

ball = cv2.imread('1.png', -1)
ball = cv2.resize(ball, (50, 50))
while True:

    r, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray', gray)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 7)
        #cv2.circle(roi_color, (5, 5), 3, (55, 25, 0), -1)
        for (ex, ey, ew, eh) in eyes:
            #cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            #cv2.circle(roi_color, (ex+int(ew/2), ey+int(eh/2)), 3, (0, 255, 0), -1)
            #pygame.draw.circle(screen, (0,255,0),(ex+int(ew/2)+x, ey+int(eh/2)+y), 3)
            #screen.blit(ball, [ex+(ew/2)+x-25, ey+(eh/2)+y-25])
            #img[y+ey-25+int(eh/2):y+ey+25+int(eh/2), x+ex+int(ew/2)-25:x+ex+int(ew/2)+25, :] = ball
            a = y + ey - 25 + int(eh / 2)
            b = x + ex + int(ew / 2) - 25
            for c in range(0, 3):
                #alpha = (ball[:, :, 3] / 255.0)
                img[a:a + 50, b:b + 50, c] = ball[:, :, c]*(ball[:, :, 3] / 255.0) + img[a:a + 50, b:b + 50, c]*(1 - (ball[:, :, 3]/ 255.0))
                #alpha and 1-alpha(beta) can be interchanged too
    cv2.imshow('img', img)
    cv2.waitKey(1)
cv2.destroyAllWindows()
