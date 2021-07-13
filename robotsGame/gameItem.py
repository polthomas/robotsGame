class GameItem(object):
    def __init__(self, xpos, ypos, look): #all items in on the game field have (x,y) and a look they are shown with
        self.xpos = xpos
        self.ypos = ypos
        self.look = look

    #def drawOnBoard(self): #puts the item into the correct position in the field 2D array
        #not going to work simply, better to just draw them all in the same refresh field function in the 
        #main program and have the bullets all in a bullets array
        #field[self.ypos][self.xpos] = self.look #but field is not accessible from here - how to fix this?


