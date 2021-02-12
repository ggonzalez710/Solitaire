from graphics import *
from button import Button
from time import *

class Cards:
    """Displays card images"""

    def __init__(self, win, center, width, height, type, number, color):
        self.win = win

        self.center = center
        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+ w, x-w
        self.ymax, self.ymin = y+h, y-h
        self.p1 = Point(self.xmin, self.ymin)
        self.p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(self.p1, self.p2)

        self.type = type
        self.number = number
        self.color = color

        self.showBack()     # Places the created card in backwards position

    def getCenter(self):
        return self.center

    def getType(self):
        return self.type

    def getNumber(self):
        return self.number

    def getColor(self):
        return self.color  

    def showBack(self):
        # Shows back side of a card
        # This function draws the back image at the card's center point
        self.backwardsCard = Image(self.center, "back.gif")
        self.backwardsCard.draw(self.win)
        self.hidden = True

    def showFront(self):
        # Shows front side of a card
        # This function draws the front image of a card at its' center point

        # Hearts
        if self.type == "Hearts":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "heartsA.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "hearts2.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "hearts3.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "hearts4.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "hearts5.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "hearts6.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "hearts7.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "hearts8.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "hearts9.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "hearts10.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "heartsJack.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "heartsQueen.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "heartsKing.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

        # Diamonds
        if self.type == "Diamonds":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamondsA.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamonds2.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamonds3.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamonds4.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamonds5.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamonds6.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamonds7.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamonds8.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamonds9.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamonds10.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamondsJack.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamondsQueen.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "diamondsKing.gif")
                self.frontCard.draw(self.win)
                self.hidden = False


        # Clubs
        if self.type == "Clubs":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubsA.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubs2.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubs3.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubs4.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubs5.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubs6.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubs7.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubs8.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubs9.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubs10.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubsJack.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubsQueen.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "clubsKing.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

        # Spades
        if self.type == "Spades":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spadesA.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spades2.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spades3.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spades4.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spades5.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spades6.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spades7.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spades8.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spades9.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spades10.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spadesJack.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spadesQueen.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "spadesKing.gif")
                self.frontCard.draw(self.win)
                self.hidden = False


    def clicked(self, p):
        "Returns true if the click is inside the card's boundaries"
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def moveCard(self, x, y):
        if self.hidden:             # If card is on its' back side, move back image
            self.backwardsCard.move(x, y)
        elif not self.hidden:       # If card is on its' front side, move front image
            self.frontCard.move(x, y)
        self.center = Point(self.center.getX() + x, self.center.getY() + y)     # Change card's center point
