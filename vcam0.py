#!/usr/bin/python
import pygame
import pygame.camera as camera
import time
import datetime
camera.init()
camlist=camera.list_cameras()
cam=camera.Camera("/dev/video0",(1600,1200),"RGB")
cam.start()
n=0
while(n!=100):
    image=cam.get_image()
    strtime=str(time.ctime())
    strname=strtime+".jpg"
    pygame.image.save(image,strname)
    time.sleep(0.5)
    n=n+1
    time.sleep(1)
cam.stop()
