import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self,mode=False,maxHands=2,detectionConf=1, trackConf=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectConf = detectionConf
        self.trackConf = trackConf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectConf,self.trackConf)
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self,frame,draw = True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        # print(result.multi_hand_landmarks)
        if self.result.multi_hand_landmarks:
            for handLmk in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handLmk, self.mpHands.HAND_CONNECTIONS)
        return frame

    def findPosition(self,frame,handNo=0, draw=True):
        lmList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(frame,(cx,cy),9,(0,255,0),cv2.FILLED)
        return lmList




def main():
    prevTime = 0
    curTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        try:
            success, frame = cap.read()
            frame = detector.findHands(frame,draw=True)
            lmList = detector.findPosition(frame, draw=True)
            if len(lmList) != 0:
                print(lmList[4])
            curTime = time.time()
            fps = 1/(curTime-prevTime)
            prevTime = curTime
            cv2.putText(frame, str(round(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
            cv2.imshow('Image', frame)
            cv2.waitKey(1)
        except Exception as e:
                print(f"Exception happened: {e}")
                continue
if __name__ == "__main__":
    main()




 # for id, lm in enumerate(handLmk.landmark):
        #     h, w, c = frame.shape
        #     cx, cy = int(lm.x*w), int(lm.y*h)
        #     print(id,cx,cy)