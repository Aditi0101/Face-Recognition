from webcam import Webcam
from detection import Detection
from effects import Effects
import cv2
 
# set up classes
webcam = Webcam()
webcam.start()
detection = Detection()
effects = Effects()
  
# loop forever
while True:
   
    # if lego policeman detected...
    image = webcam.get_current_frame()
    item_detected = detection.is_item_detected_in_image('haarcascade_frontalface_default.xml', image)
   
    # ...then draw a virtual jail for all those nasty criminals
    if item_detected:
        effects.render(image)
                      
    # show the scene
    cv2.imshow('scene',image)
    cv2.waitKey(100)