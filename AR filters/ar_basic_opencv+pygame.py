import numpy as np
import cv2
import pygame

pygame.init()

cap = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:

    r, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    #print(img.shape[:2])
    #bg = pygame.image.load(pygame.surfarray.make_surface(img))
    img1 = np.rot90(img)
    img1 = cv2.flip(img1, 0)
    screen = pygame.display.set_mode(img.shape[:2])
    #pygame.display.flip()
    screen.blit(pygame.surfarray.make_surface(img1), [0, 0])
    ball = pygame.image.load('1.png')
    ball = pygame.transform.scale(ball, [50, 50])

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        cv2.circle(roi_color, (5, 5), 3, (55, 25, 0), -1)
        pygame.draw.circle(screen, (55, 25, 0), (5, 5), 3)
        print(eyes)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.circle(roi_color, (ex+int(ew/2),ey+int(eh/2)), 3, (0,255,0), -1)
            pygame.draw.circle(screen, (0,255,0),(ex+int(ew/2)+x, ey+int(eh/2)+y), 3)
            screen.blit(ball, [ex+(ew/2)+x-25, ey+(eh/2)+y-25])
    pygame.display.update()
    cv2.imshow('img', img)
    cv2.waitKey(1)
cv2.destroyAllWindows()
