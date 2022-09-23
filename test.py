import cv2
capture =cv2.VideoCapture(0)
salida=cv2.VideoWriter("test.avi",cv2.VideoWriter_fourcc(*'XVID'),30,(640,480))

while True:
    ret, frame=capture.read()
    cv2.imshow("ventana",frame)
    salida.write(frame)
    if(cv2.waitKey(1)==ord('q')):
        break

salida.release()
capture.release()
cv2.destroyAllWindows()
