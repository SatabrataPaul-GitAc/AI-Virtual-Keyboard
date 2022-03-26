import cv2
from cvzone.HandTrackingModule import HandDetector
from button import Button

capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=2)

button_list = []
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

for i in range(len(keys)):
    for x, k in enumerate(keys[i]):
        button_list.append(Button((100*x+50, 100*i+50), k))


while True:
    success, img = capture.read()
    hands, img = detector.findHands(img)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1['lmList']
        bbox1 = hand1['bbox']
        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2['lmList']
            bbox2 = hand2['bbox']
            fingers2 = detector.fingersUp(hand2)

    for obj in button_list:
        img = obj.draw_button(img)
    cv2.imshow("Myimage", img)
    cv2.waitKey(2)
