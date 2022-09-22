import cv2

capture = cv2.VideoCapture(1)
#objeto salida, contiene los parámetros para crear el video
salida = cv2.VideoWriter('webCam.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (640,480))

while (True):
    ret, frame = capture.read()
    cv2.imshow('frame',frame)
    #Usar write para GUARDAR el video
    salida.write(frame)
    if (cv2.waitKey(1) == ord('s')):
        break

salida.release()
capture.release()
cv2.destroyAllWindows()