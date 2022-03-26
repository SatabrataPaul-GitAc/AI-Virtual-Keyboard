import cv2


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

    def draw_button(self, img):
        x, y = self.pos
        w, h = self.size
        cv2.rectangle(img, self.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, self.text, (x + 20, y + 65), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255),
                    5)
        return img
