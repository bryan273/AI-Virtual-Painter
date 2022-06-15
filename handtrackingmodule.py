import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComplexity=1 ,detectionCon=0.5, trackCon=0.5):
        # parameter untuk deteksi hand
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands 
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
        self.detectionCon, self.trackCon) # deteksi hand
        self.mpDraw = mp.solutions.drawing_utils 
        self.tipIds = [4, 8, 12, 16, 20]

    # nemuin tangan dan gambar line di tangan
    def findHands(self, img, draw=True):
        # imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # ubah ke RGB
        self.results = self.hands.process(img) # result dari posisi tangan dll

        if self.results.multi_hand_landmarks: 
            for handLms in self.results.multi_hand_landmarks: # handLms -> berapa tangan yg kedetect
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                    self.mpHands.HAND_CONNECTIONS) # gambar dot and line di tangan

        return img

    # cari posisi tangan dan gambar kotak 
    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h) # posisi tangan sumbu x y 
                xList.append(cx)
                yList.append(cy)
                self.lmList.append([id, cx, cy]) # append posisi tangan
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)

            if draw:
                cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                (0, 255, 0), 2) # gambar kotak di tangan

        return self.lmList

    # cek apakah jari naik
    def fingersUp(self):
        fingers = []
        # Thumb yg naik
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Fingers yg naik
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

# test hand detection
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
    detector = handDetector()
    while True:
        _, img = cap.read()

        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
        (255, 0, 255), 3) # Cek fps 

        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
