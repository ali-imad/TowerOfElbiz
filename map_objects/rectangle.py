class Rect:
    def __init__(self, x, y, w, h):
        """
        x1 = left
        x2 = right
        y1 = top
        y2 = bottom
        """

        self.x1 = x
        self.x2 = x + w
        self.y1 = y
        self.y2 = y + h

    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return (center_x, center_y)

    def intersect(self, other):
        """
        Returns true if self is within the other rectangle
        see rect_intersect_demo.png for visual demonstration of a "true" condition
        :return: bool
        """

        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)
