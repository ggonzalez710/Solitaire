#This is just a practice.
from graphics import *
class Cards:

    def __init__(self):
        
         self.Window=GraphWin("Solitary",800,800)
         self.Window.setCoords(0,0,800,800)
         self.card=Rectangle(Point(300,400),Point(400,600))
         self.card.setFill("blue")
         self.card.setOutline("black")
         
    def getCard(self):
        return self.card
    def setCardsize(self,pi,p2):
        self.card=Rectangle(p1,p2)
    

        
if __name__ == "__main__":

    pass
