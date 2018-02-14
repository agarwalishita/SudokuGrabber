import cv2
import numpy as np
    
img = cv2.imread('/Users/Ishitaagarwal/Documents/GitHub/SudokuGrabber/GrabIt/su.jpg')
# imp=img
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
t_gray = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.adaptiveThreshold(t_gray,255,1,1,5,2)
cv2.imshow('thresh',thresh)
r,contours,h = cv2.findContours(thresh,1,2) #closed figures
print (len(contours))
max_area = 0
 
biggest=0
font = cv2.FONT_HERSHEY_SIMPLEX
for cnt in contours:
        
    area = cv2.contourArea(cnt)
    if area > 100:
        peri = cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        
                
        if area > max_area and len(approx)==4:
            biggest = approx
            max_area = area
            a=cnt
print (biggest) 
    #print (biggest[0][0][1])
cv2.drawContours(img,[a],0,(0,255,0),2)
    #crop_img = img[63:387, 43:375] 
    
    #cv2.imshow("cropped", crop_img)
x, y, w, h = cv2.boundingRect(a)
roi = img[y:y+h, x:x+w] #stores the cropped image
cv2.imshow('roi',roi)
ro = thresh[y:y+h, x:x+w]
cv2.imshow('ro',ro) #(stores cropped thresh image)
    
    
edges = cv2.Canny(ro,50,150,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180,135)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    
    cv2.line(roi,(x1,y1),(x2,y2),(0,0,255),2)
    print (x1)

    
    # cv2.putText(imp,'*',(x1,y1), font, 4,(255,255,255),2,cv2.LINE_AA)
    #cv2.imshow('houghlines3.jpg', img)
    
        
        
cv2.imshow('roi',roi)
    #cv2.imshow('gray',gray)
# cv2.imshow('img',img)
# cv2.imshow('imp',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    