import keyboard
import time     
from robot import Robot
from bullet import Bullet
from gameItem import GameItem

global field
field = []

global bullets
bullets = []

def refreshField(robot1,robot2): #redraws the playing field with all items in their updated positions
  field = [["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
           ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
           ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
           ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
           ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
           ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
           ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
           ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
           ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
           ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]] #10x10

 # robot1.drawOnBoard()
 # robot2.drawOnBoard()
  field[robot1.ypos][robot1.xpos] = " P " #putting robots in their positions
  field[robot2.ypos][robot2.xpos] = " M "

  for bul in bullets:
      field[bul.ypos][bul.xpos] = " o "

  print("______________________________") #line to mark top of field
  for i in range(10): #drawing playing field from the field array
    for j in range(10):
      print(field[i][j], end = "")
    print("\n")


#initiating instances of robots and bullets to be used in the game:

robot1 = Robot("Pippin", 980, 7000, 6, 7, ['w','a','s','d','q','e'], " P ", bullets)
robot2 = Robot("Merry", 567, 8462, 8, 2, ['i','j','k','l','u','o'], " M ", bullets)

while True: #forever loop to keep updating game and checking keypresses
  robot1.beControlled()
  robot2.beControlled()
  refreshField(robot1,robot2)
  time.sleep(0.1)


