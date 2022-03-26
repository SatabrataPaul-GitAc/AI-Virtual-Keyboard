import cv2
from cvzone.HandTrackingModule import HandDetector
from button import Button

capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=2)
mybutton1 = Button([100, 100], 'Q')
mybutton2 = Button([230, 100], 'W')
mybutton3 = Button([360, 100], 'E')
mybutton4 = Button([490, 100], 'R')
mybutton5 = Button([620, 100], 'T')
mybutton6 = Button([750, 100], 'Y')
mybutton7 = Button([880, 100], 'U')
mybutton8 = Button([1010, 100], 'I')
mybutton9 = Button([100, 230], 'O')
mybutton10 = Button([230, 230], 'P')



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
    img = mybutton1.draw_button(img)
    img = mybutton2.draw_button(img)
    img = mybutton3.draw_button(img)
    img = mybutton4.draw_button(img)
    img = mybutton5.draw_button(img)
    img = mybutton6.draw_button(img)
    img = mybutton7.draw_button(img)
    img = mybutton8.draw_button(img)
    img = mybutton9.draw_button(img)
    img = mybutton10.draw_button(img)
    cv2.imshow("Myimage", img)
    cv2.waitKey(2)
