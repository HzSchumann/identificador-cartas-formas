#Nome: Matheus Santana de Oliveira RM: 79907
#Nome: Gustavo Canola Almeida RM: 83413
#Nome: Diego Rossi RM: 83864
#Nome: Tainnah Chagas RM: 83751
#Nome: Lucas Thomazella e Silva RM: 82057
        
import cv2
import numpy as np
import imutils

cap  =  cv2.VideoCapture('q1B.mp4')
cap.set(3,640)
cap.set(4,480)

while True :

    _, frame  =  cap.read()

    #Seu código aqui......
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([79,100,138]) 
    upper_blue = np.array([124,158,214])

    lower_orange = np.array([2,108,204])
    upper_orange = np.array([22,128,284])

    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_orange, upper_orange)

    cnts = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)

    for c in cnts:
        area = cv2.contourArea(c)
        if area > 10000:
            print(area)
            
            if area == 93306.5 :
                cv2.putText(frame, "Colisao Detectada", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255), 3)
                print("Colisao Detectada")
            if area == 93306.5:
                cv2.putText(frame, "Colisao Detectada", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255), 3)
                print("Colisao Detectada")
            if area == 93233.5:
                cv2.putText(frame, "Colisao Detectada", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255), 3)
                print("Colisao Detectada")
            if area == 91316.5:
                cv2.putText(frame, "ultrapassou completamente a outra forma geométrica", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255), 3)
                print("ultrapassou completamente a outra forma geométrica")
            if area == 91786.0:
                cv2.putText(frame, "ultrapassou completamente a outra forma geométrica", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255), 3)
                print("ultrapassou completamente a outra forma geométrica")
            if area == 91946.0:
                cv2.putText(frame, "ultrapassou completamente a outra forma geométrica", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,255,255), 3)
                print("ultrapassou completamente a outra forma geométrica")
        
                
            
            cv2.drawContours(frame,[c],-1,(0,255,0), 7)

            M = cv2.moments(c)

            cx = int(M["m10"]/ M["m00"])
            cy = int(M["m01"]/ M["m00"])

            cv2.circle(frame,(cx,cy),9,(255,255,255),-3)
            cv2.putText(frame, "", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5, (255,0,255), 3)

        for c in cnts2:
            area_orange = cv2.contourArea(c)
            if area_orange > 5000:

                cv2.drawContours(frame, [c], -1, (0,255,0), 3)

              
                
        
    #Exibe resultado
    cv2.imshow("Feed",frame)

    # Aguardar a saída da tecla 'ESC'
    k =  cv2.waitKey(5)
    if k ==  27:
        break

# É assim que você sai
tampa.liberar ()
cv2.destroyAllWindows()