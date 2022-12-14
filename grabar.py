import cv2
import time
import os

#funcion para obtener fecha y hora en string
def fecha_hora():
    fecha = time.strftime("%Y-%m-%d")
    hora = time.strftime("%H-%M-%S")
    return fecha + '_' + hora

#convierte las horas y minutos a segundos
def duracion(h,m,s):
    return h*3600+m*60+s

#indica si se debe continuar grabando
continuar = True
#directorio donde se guardaran los videos
dirVideos ='/home/jetnano/Desktop/Dashcam/videos'
#crear directorio si no existe
if not os.path.exists(dirVideos):
    os.makedirs(dirVideos)

#iniciamos la grabacion
while continuar:
    cam = cv2.VideoCapture(0)
    #eliminar el ultimo video
    if len(os.listdir(dirVideos)) > 12:
        os.remove(dirVideos+'/'+os.listdir(dirVideos)[0])
    # Inicializar el grabador
    out=cv2.VideoWriter(dirVideos+'/'+fecha_hora()+'.mp4',cv2.VideoWriter_fourcc(*'mp4v'),10,(1280,720))
    # Grabar durante 5 segundos
    t_end = time.time() + duracion(0,1,0)
    numFrames=0
    while (time.time() < t_end):
        ret, frame = cam.read()
        numFrames+=1
        print(numFrames)
        cv2.imshow('frame',frame)
        out.write(frame)
        if(cv2.waitKey(1) == ord('q')):
            continuar=False
            break
        #cv2.waitKey(50)
    # Liberar la camara y el grabador
    out.release()
    cam.release()

