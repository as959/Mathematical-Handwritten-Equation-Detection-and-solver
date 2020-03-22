##Canvas (Paint) Application in python to input equation from user ##
##Exit using Esc key ##

#importing libraries

import cv2
import numpy as np
drawing = False  # true if mouse is pressed
mode = True


# mouse callback function

def paint_draw(event, former_x, former_y, flags, param):
    global current_former_x, current_former_y, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        current_former_x, current_former_y = former_x, former_y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.line(image, (current_former_x, current_former_y), (former_x, former_y), (0, 0, 0), 1)
                current_former_x = former_x
                current_former_y = former_y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.line(image, (current_former_x, current_former_y), (former_x, former_y), (0, 0, 0), 1)
            current_former_x = former_x
            current_former_y = former_y
    return former_x, former_y

#canvas application

image = cv2.imread("white_base.png")  #specify image name in current directory
cv2.namedWindow("OpenCV Paint Brush")
cv2.setMouseCallback('OpenCV Paint Brush', paint_draw)
while True:
    cv2.imshow('OpenCV Paint Brush', image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # Escape KEY to exit canvas
        cv2.imshow("final_paint", image)
        cv2.waitKey(1)
        cv2.imwrite("painted_image.jpg", image)  #Imputed image saved in currect directory 
        break
cv2.destroyAllWindows()
