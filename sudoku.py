    import cv2
    import numpy as np
    
    
    img = cv2.imread('/Users/Ishitaagarwal/Desktop/su.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.adaptiveThreshold(gray,255,1,1,5,2)
    cv2.imshow('thresh',thresh)
    r,contours,h = cv2.findContours(thresh,1,2) #closed figures
    print (len(contours))
    max_area = 0
    biggest=0
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
    crop_img = img[63:387, 43:375] 
    
    #cv2.imshow("cropped", crop_img)
    x, y, w, h = cv2.boundingRect(a)
    roi = img[y:y+h, x:x+w]
    cv2.imshow('roi',roi)
    ro = thresh[y:y+h, x:x+w]
    cv2.imshow('ro',ro)
    
        
        
    cv2.imshow('img',img)
    #cv2.imshow('gray',gray)
    #cv2.imshow('thresh',thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    