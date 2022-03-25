import cv2
from cvzone.HandTrackingModule import HandDetector
capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = capture.read()
    hands, img = detector.findHands(img)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1['lmList']
        bbox1 = hand1['bbox']
        fingers1 = detector.fingersUp(hand1)

        if len(hands)==2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2['lmList']
            bbox2 = hand2['bbox']
            fingers2 = detector.fingersUp(hand2)

    cv2.imshow("Myimage", img)
    cv2.waitKey(2)