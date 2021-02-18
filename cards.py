from graphics import *
from button import Button
from time import *

class Cards:
    """Displays card images"""

    def __init__(self, win, center, width, height, types, number, color):

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        
        self.win = win
        self.rect = Rectangle(p1, p2)
        self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
        self.grabber.setFill('red')

        self.types = types
        self.number = number
        self.color = color
        self.hidden = True
        self.backwardsCard = Image(self.rect.getCenter(), "Card Images/back.gif")
        self.frontCard = Image(self.rect.getCenter(), "Card Images/heartsA.gif")

    def getCenter(self):
        return self.rect.getCenter()

    def getType(self):
        return self.types

    def getNumber(self):
        return self.number

    def getColor(self):
        return self.color
    def getHidden(self):
        return self.hidden

    def showBack(self):
        # Shows back side of a card
        # This function draws the back image at the card's center point
        self.backwardsCard = Image(self.rect.getCenter(), "Card Images/back.gif")
        self.backwardsCard.draw(self.win)
        self.hidden = True

    def showFront(self):
        # Shows front side of a card
        # This function draws the front image of a card at its' center point

        # Hearts
        if self.types == "Hearts":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/heartsA.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/hearts2.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/hearts3.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/hearts4.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/hearts5.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/hearts6.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/hearts7.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/hearts8.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/hearts9.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/hearts10.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/heartsJack.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/heartsQueen.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/heartsKing.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

        # Diamonds
        if self.types == "Diamonds":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamondsA.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamonds2.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamonds3.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamonds4.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamonds5.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamonds6.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamonds7.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamonds8.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamonds9.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamonds10.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamondsJack.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamondsQueen.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/diamondsKing.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False


        # Clubs
        if self.types == "Clubs":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubsA.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubs2.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubs3.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubs4.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubs5.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubs6.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubs7.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubs8.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubs9.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubs10.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubsJack.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubsQueen.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/clubsKing.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

        # Spades
        if self.types == "Spades":
            if self.number == 1:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spadesA.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 2:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spades2.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 3:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spades3.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 4:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spades4.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 5:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spades5.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 6:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spades6.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 7:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spades7.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 8:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spades8.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 9:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spades9.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 10:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spades10.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 11:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spadesJack.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 12:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spadesQueen.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False

            elif self.number == 13:
                self.backwardsCard.undraw()
                self.frontCard = Image(self.rect.getCenter(), "Card Images/spadesKing.gif")
                self.frontCard.draw(self.win)
                #self.grabber = Circle(Point(self.xmax - 10, self.ymax - 10), 5)
                #self.grabber.setFill('red')
                self.grabber.draw(self.win)
                self.hidden = False


    def card_click(self, p):
        "Returns true if the click is inside the card's boundaries"
        return (self.grabber.getP1().getX() <= p.getX() <= self.grabber.getP2().getX()) and (self.grabber.getP1().getY() <= p.getY() <= self.grabber.getP2().getY())

    def moveCard_Start(self, x, y):
        if self.hidden:             # If card is on its' back side, move back image
            self.rect.move(x, -y)
            self.backwardsCard.move(x, -y)
        elif not self.hidden:       # If card is on its' front side, move front image
            self.rect.move(x, -y)
            self.frontCard.move(x, -y)
            self.grabber.move(x, -y)
