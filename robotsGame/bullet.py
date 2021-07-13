from gameItem import GameItem

class Bullet(GameItem):
    def __init__(self, xpos, ypos, look, direction):
        super().__init__(xpos, ypos)
        self.look = " o "
        self.direction = direction

    def move(self): #will continue to move in direction it was shot in until a collision occurs
        if self.direction == "left":
            self.xpos -= 1
        else:
            self.xpos += 1

