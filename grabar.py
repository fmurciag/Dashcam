import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import time
import os
import numpy as np

# Inicializar la cámara
cam = cv2.VideoCapture(1)
dirVideos ='C:/Users/FRAN/Desktop/Sistema-de-video-continuo/videos'
#suncion para obtener fecha y hora en string
def fecha_hora():
    fecha = time.strftime("%Y-%m-%d")
    hora = time.strftime("%H-%M-%S")
    return fecha + '_' + hora

#funcion para grabar video
def grabar():
    # Inicializar el grabador
    fourcc = VideoWriter_fourcc(*'MP42')
    out = VideoWriter(dirVideos+'/'+fecha_hora()+'.avi', fourcc, 20.0, (640, 480))
    # Grabar durante 5 segundos
    t_end = time.time() + 5
    while time.time() < t_end:
        ret, frame = cam.read()
        cv2.imshow("frame",frame)
        out.write(frame)
    # Liberar la cámara y el grabador
    out.release()

if __name__ == '__main__':
    numVideos=0
    while True:
        numVideos = len(os.listdir(dirVideos))
        #eliminar el ultimo video
        if len(os.listdir(dirVideos)) > 5:
            os.remove(dirVideos+'/'+os.listdir(dirVideos)[0])
        grabar()
    cam.release()

