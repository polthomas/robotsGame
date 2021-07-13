import keyboard
from gameItem import GameItem

class Robot(GameItem):
    def __init__(self, name, ammo, lives, xpos, ypos, controls, look, bullets):
        super().__init__(xpos, ypos, look)
        self.name = name
        self.ammo = ammo
        self.lives = lives
        self.controls = controls
        self.bullets = bullets

    def beControlled(self): #robot moving when movement keys are pressed
        if keyboard.is_pressed(self.controls[0]):
            if self.ypos != 0: #can't move off edges of field
                self.ypos -= 1
        if keyboard.is_pressed(self.controls[1]):
            if self.xpos != 0:
                self.xpos -= 1
        if keyboard.is_pressed(self.controls[2]):
            if self.ypos != 9:
                self.ypos += 1
        if keyboard.is_pressed(self.controls[3]):
            if self.xpos != 9:
                self.xpos += 1
        if keyboard.is_pressed(self.controls[4]): #when shoot keys are pressed
            self.shoot("left")
        if keyboard.is_pressed(self.controls[5]):
            self.shoot("right")

    def shoot(self, direction): #adds the new instance of a bullet to the bullet array
        self.bullets.append(Bullet(self.xpos, self.ypos, " o ", direction))




