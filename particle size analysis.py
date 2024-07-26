from cmath import rect
import cv2
from object_detector import *  
import numpy as np




#load aruco detector 
parameters = cv2.aruco.DetectorParameters()
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)


#load object detector
detector = HomogeneousBgDetector()

img = cv2.imread("images/4x4_50(sample7).jpg")

corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)


int_corners = np.int0(corners)

cv2.polylines(img, int_corners, True, (0, 255, 0), 5)





#aruco perimeter

aruco_perimeter = cv2.arcLength(corners[0], True)


print(aruco_perimeter)

#pixel to cm

pixel_cm_ratio = aruco_perimeter/ 125  


contours = detector.detect_objects(img)
#print(contours) 

#draw poly
for cnt in contours:

    #draw rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    object_width = w/ pixel_cm_ratio
    object_height = h/ pixel_cm_ratio

    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 10, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {} mm".format(round(object_width, 1)), (int(x-50), int(y-20)), cv2.FONT_HERSHEY_COMPLEX , 1.5, (0, 255, 0), 3)
    cv2.putText(img, "Height {} mm".format(round(object_height, 1)), (int(x-50), int(y+30)), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 255), 3)
    
    #print(box)
 


resized_width = 1200
resized_height = 800
resized_image = cv2.resize(img, (resized_width, resized_height))

cv2.imshow("image", resized_image)
cv2.waitKey(0)
