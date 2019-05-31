"""
Creats rectangle shaped room
X / Y are starting cords (start is wall)
W / H are ending cords (end is wall)
"""
class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x     #x start
        self.y1 = y     #y start
        self.x2 = x + w #x end
        self.y2 = y + h #y end