import cv2


class Button():
    def __init__(self, pos, text, size=[100, 100]):
        self.pos = pos
        self.size = size
        self.text = text

    def draw_button(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0]+self.size[0], self.pos[1]+self.size[1]), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, self.text, (self.pos[0] + 25, self.pos[1] + 72), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255),
                    5)
        return img
