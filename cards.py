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
        self.backwardsCard = Image(self.center, "Card Images/back.gif")
        self.backwardsCard.draw(self.win)
        self.hidden = True

    def showFront(self):
        # Shows front side of a card
        # This function draws the front image of a card at its' center point

        # Hearts
        if self.type == "Hearts":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/heartsA.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/hearts2.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/hearts3.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/hearts4.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/hearts5.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/hearts6.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/hearts7.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/hearts8.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/hearts9.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/hearts10.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/heartsJack.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/heartsQueen.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/heartsKing.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

        # Diamonds
        if self.type == "Diamonds":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamondsA.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamonds2.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamonds3.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamonds4.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamonds5.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamonds6.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamonds7.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamonds8.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamonds9.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamonds10.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamondsJack.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamondsQueen.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/diamondsKing.gif")
                self.frontCard.draw(self.win)
                self.hidden = False


        # Clubs
        if self.type == "Clubs":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubsA.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubs2.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubs3.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubs4.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubs5.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubs6.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubs7.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubs8.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubs9.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubs10.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubsJack.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubsQueen.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/clubsKing.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

        # Spades
        if self.type == "Spades":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spadesA.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spades2.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spades3.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spades4.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spades5.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spades6.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spades7.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spades8.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spades9.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spades10.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spadesJack.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spadesQueen.gif")
                self.frontCard.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.center, "Card Images/spadesKing.gif")
                self.frontCard.draw(self.win)
                self.hidden = False


    def clicked(self, p):
        "Returns true if the click is inside the card's boundaries"
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def moveCard(self, x, y):
        if self.hidden:             # If card is on its' back side, move back imag
            self.backwardsCard.move(x, y)
        elif not self.hidden:       # If card is on its' front side, move front image
            self.frontCard.move(x, y)
        self.center = Point(self.center.getX() + x, self.center.getY() + y)     # Change card's center point
