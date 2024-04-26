#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import imutils

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture("q2.mp4")



while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    # Seu código aqui....... 
    contours_count = 0
    contoursb_count = 0

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_border = np.array([-10,-10,118])
    upper_border = np.array([10,10,198])

    lower_blue = np.array([98,96,159])
    upper_blue = np.array([118,116,239])

    mask_border = cv2.inRange(hsv, lower_border, upper_border)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    cnts_border = cv2.findContours(mask_border, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts_border = imutils.grab_contours(cnts_border)

    cnts_blue = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts_blue = imutils.grab_contours(cnts_blue)

    for c in cnts_border:
        area_border = cv2.contourArea(c)
        if area_border > 3000:

            cv2.drawContours(frame, [c], -1, (0,255,0), 3)
            
            M = cv2.moments(c)
            

            x,y,w,h = cv2.boundingRect(c)
            # img = cv2.rectangle(frame,(x+10,y+15),(x+(w-235),y+(h-325)),(0,255,0),1,cv2.LINE_AA)
            roi = frame[y+25:y+h-330, x+20:x+w-235]
            roib = frame[y+15:y+h-325, x+20:x+w-245]

            hsv2 = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            hsv3 = cv2.cvtColor(roib, cv2.COLOR_BGR2HSV)

            lower_red = np.array([0,50,207])
            upper_red = np.array([10,255,255])

            lower_black = np.array([0,0,0])
            upper_black = np.array([50,50,100])

            mask_red = cv2.inRange(hsv2, lower_red, upper_red)
            mask_black = cv2.inRange(hsv3, lower_black, upper_black)

            cnts_red,_ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            cnts_black,_ = cv2.findContours(mask_black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            if cnts_black is None:
                cnts_black = []

            if cnts_red is None:
                cnts_red = []

            for cn in cnts_red:
                area_red = cv2.contourArea(cn)
                if area_red > 70:
                    cv2.drawContours(roi, [cn], -1, (0,255,0), 3)
                    contours_count += 1

                    cx = int(M["m10"]/ M["m00"])
                    cy = int(M["m01"]/ M["m00"])

                    cv2.circle(frame, (cx,cy),7,(0,0,255), -1)
                    cv2.putText(frame, "Vermelho", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (0,0,255), 3)   


            for cn in cnts_black:
                area_black = cv2.contourArea(cn)
                if area_black > 50:
                    cv2.drawContours(roib, [cn], -1, (252,3,232), 3)
                    contoursb_count += 1

                    cx = int(M["m10"]/ M["m00"])
                    cy = int(M["m01"]/ M["m00"])

                    cv2.circle(frame, (cx,cy),7,(0,0,0), -1)
                    cv2.putText(frame, "Preto", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (0,0,0), 3)   


            
    cv2.putText(frame, f'Vermelho: {contours_count}', (5, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)  
    cv2.putText(frame, f'Preto: {contoursb_count}', (5, 70), font, 1, (0, 0, 0), 2, cv2.LINE_AA)     
    # Exibe resultado
    
    cv2.imshow("Feed", frame)
    

    # Wait for key 'ESC' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# That's how you exit
cap.release()
cv2.destroyAllWindows()