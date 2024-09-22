import cv2
import mediapipe
import numpy as np
import time
import handTracking_module as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

Wcam, Hcam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, Wcam)
cap.set(4, Hcam)
prevTime = 0
curTime = 0

detector = htm.HandDetector()


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
vol = 0
volBar = 400
volPer = 0
Minvol = volRange[0]
Maxvol = volRange[1]



while True:
    try:
        succes, frame = cap.read()
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame,draw=False)
        if len(lmList) != 0:
            # print(lmList[4],lmList[8])
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cx, cy = (x1 + x2) //2, (y1 + y2)//2


            cv2.circle(frame,(x1,y1),15,(255,0,255),cv2.FILLED)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
            cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),3)
            cv2.circle(frame,(cx, cy),10,(255,0,255),cv2.FILLED)

            length = math.hypot(x2 - x1, y2 - y1)
            # print(length)

            vol = np.interp(length,[50,300],[Minvol,Maxvol])
            volBar = np.interp(length,[50,300],[400,150])
            volPer = np.interp(length,[50,300],[0,100])
            print(int(length),vol)
            volume.SetMasterVolumeLevel(vol,None)

            if length<50:
                cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

        cv2.rectangle(frame,(50,150),(85,400),(0,255,0),3)
        cv2.rectangle(frame, (50, int(volBar)), (85, 400), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame,f'VOL: {int(volPer)}%',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)


        curTime = time.time()
        fps = 1/(curTime-prevTime)
        prevTime = curTime

        cv2.putText(frame,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
        cv2.imshow('frame',frame)
        cv2.waitKey(1)
    except Exception as e:
        print(f"Exception happened: {e}")
        continue