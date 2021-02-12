from graphics import *
from button import Button
from cards import Cards
from time import *
import random
import playsound

class Solitaire:

    def __init__(self):
        self.StartMenu()

        self.win = GraphWin("Solitaire", 1400, 800)
        self.win.setBackground("green")

        self.Time = Button(self.win, Point(500, 30), 120, 50, "Time")
        self.Time.activate()

        self.Score = Button(self.win, Point(1200, 30), 120, 50, "Score")
        self.Score.activate()

        """
        self.firstCol = Cards(self.win, Point(250, 400), 100, 150)#, "1st column")  # add +150 pixel in the x value for all
        self.secondCol = Cards(self.win, Point(400, 400), 100, 150)#, "2nd column")
        self.thirdCol = Cards(self.win, Point(550, 400), 100, 150)#, "3rd column")
        self.fourthCol = Cards(self.win, Point(700, 400), 100, 150)#, "4th column")
        self.fifthCol = Cards(self.win, Point(850, 400), 100, 150)#, "5th column")
        self.sixthCol = Cards(self.win, Point(1000, 400), 100, 150)#, "6th column")
        self.seventhCol = Cards(self.win, Point(1150, 400), 100, 150)#, "7th column")

        
        self.randomCards.activate()
        self.firstCol.activate()
        self.secondCol.activate()
        self.thirdCol.activate()
        self.fourthCol.activate()
        self.fifthCol.activate()
        self.sixthCol.activate()
        self.seventhCol.activate()
        """

        self.foundationPiles1 = Button(self.win, Point(700, 150), 100, 150, "Foundation")  # add +150 pixel in the x value for all
        self.foundationPiles1.activate()
        self.foundationPiles2 = Button(self.win, Point(850, 150), 100, 150, "Foundation")
        self.foundationPiles2.activate()
        self.foundationPiles3 = Button(self.win, Point(1000, 150), 100, 150, "Foundation")
        self.foundationPiles3.activate()
        self.foundationPiles4 = Button(self.win, Point(1150, 150), 100, 150, "Foundation")
        self.foundationPiles4.activate()

        self.QuitButton = Button(self.win, Point(1130, 600), 120, 50, "Quit")
        self.QuitButton.activate()

        self.UndoButton = Button(self.win, Point(1000, 600), 120, 50, "Undo")
        self.UndoButton.activate()

        self.create_cards(self.win)

        while True:
            p = self.win.getMouse()
            #if self.randomCards.clicked(p):
                #print("Touching random cards ")
                #randomCards.moveCardCard(75, 125)
                #sleep(1)
                #randomCards.moveCardCard(75, 125)

            #if self.randomCards[0].clicked(p):
                #print("Touchng hearts A")

                #randomCards_img.randomized_deck(win, 250, 400)
            #if self.randomCards.clicked(p):
                #print("Touching random cards ")
            """
            if self.firstCol.clicked(p):
                print("Touching first column ")
            elif self.secondCol.clicked(p):
                print("Touching second column ")
            elif self.thirdCol.clicked(p):
                print("Touching third column ")
            elif self.fourthCol.clicked(p):
                print("Touching fourth column ")
            elif self.fifthCol.clicked(p):
                print("Touching fifth column ")
            elif self.sixthCol.clicked(p):
                print("Touching sixth column ")
            elif self.seventhCol.clicked(p):
                print("Touching seventh column ")
            elif self.foundationPiles1.clicked(p):
                print("Touching first foundation pile ")
            elif self.foundationPiles2.clicked(p):
                print("Touching second foundation pile ")
            elif self.foundationPiles3.clicked(p):
                print("Touching third foundation pile ")
            elif self.foundationPiles4.clicked(p):
                print("Touching fourth foundation pile ")
            elif self.Time.clicked(p):
                print("Touching time section ")
            elif self.Score.clicked(p):
                print("Touching score section ")
            elif self.UndoButton.clicked(p):
                print("Touching Undo Button")
            """
            if self.QuitButton.clicked(p):
                self.win.close()
            #else:
                #for i in range(28):
                #    if self.stockpile[i].clicked(p):
                #        self.stockpile[i].showFront()


    def create_cards(self, win):
        stockpile_position = Point(100, 150) # Starting position of the entire deck
        self.stockpile = []

        # Hearts Cards
        #self.hearts = []
        self.heartsA = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 1, "Red")
        self.hearts2 = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 2, "Red")
        self.hearts3 = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 3, "Red")
        self.hearts4 = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 4, "Red")
        self.hearts5 = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 5, "Red")
        self.hearts6 = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 6, "Red")
        self.hearts7 = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 7, "Red")
        self.hearts8 = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 8, "Red")
        self.hearts9 = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 9, "Red")
        self.hearts10 = Cards(self.win, stockpile_position, 100, 150, "Hearts", 10, "Red")
        self.heartsJ = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 11, "Red")
        self.heartsQ = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 12, "Red")
        self.heartsK = Cards(self.win,  stockpile_position, 100, 150, "Hearts", 13, "Red")
        self.stockpile.append(self.heartsA)
        self.stockpile.append(self.hearts2)
        self.stockpile.append(self.hearts3)
        self.stockpile.append(self.hearts4)
        self.stockpile.append(self.hearts5)
        self.stockpile.append(self.hearts6)
        self.stockpile.append(self.hearts7)
        self.stockpile.append(self.hearts8)
        self.stockpile.append(self.hearts9)
        self.stockpile.append(self.hearts10)
        self.stockpile.append(self.heartsJ)
        self.stockpile.append(self.heartsQ)
        self.stockpile.append(self.heartsK)

        # Diamonds Cards
        #self.diamonds = []
        self.diamondsA = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 1, "Red")
        self.diamonds2 = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 2, "Red")
        self.diamonds3 = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 3, "Red")
        self.diamonds4 = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 4, "Red")
        self.diamonds5 = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 5, "Red")
        self.diamonds6 = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 6, "Red")
        self.diamonds7 = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 7, "Red")
        self.diamonds8 = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 8, "Red")
        self.diamonds9 = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 9, "Red")
        self.diamonds10 = Cards(self.win,   stockpile_position, 100, 150, "Diamonds", 10, "Red")
        self.diamondsJ = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 11, "Red")
        self.diamondsQ = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 12, "Red")
        self.diamondsK = Cards(self.win,    stockpile_position, 100, 150, "Diamonds", 13, "Red")
        self.stockpile.append(self.diamondsA)
        self.stockpile.append(self.diamonds2)
        self.stockpile.append(self.diamonds3)
        self.stockpile.append(self.diamonds4)
        self.stockpile.append(self.diamonds5)
        self.stockpile.append(self.diamonds6)
        self.stockpile.append(self.diamonds7)
        self.stockpile.append(self.diamonds8)
        self.stockpile.append(self.diamonds9)
        self.stockpile.append(self.diamonds10)
        self.stockpile.append(self.diamondsJ)
        self.stockpile.append(self.diamondsQ)
        self.stockpile.append(self.diamondsK)

        # Clubs Cards
        #self.clubs = []
        self.clubsA = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 1, "Black")
        self.clubs2 = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 2, "Black")
        self.clubs3 = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 3, "Black")
        self.clubs4 = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 4, "Black")
        self.clubs5 = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 5, "Black")
        self.clubs6 = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 6, "Black")
        self.clubs7 = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 7, "Black")
        self.clubs8 = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 8, "Black")
        self.clubs9 = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 9, "Black")
        self.clubs10 = Cards(self.win,  stockpile_position, 100, 150, "Clubs", 10, "Black")
        self.clubsJ = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 11, "Black")
        self.clubsQ = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 12, "Black")
        self.clubsK = Cards(self.win,   stockpile_position, 100, 150, "Clubs", 13, "Black")
        self.stockpile.append(self.clubsA)
        self.stockpile.append(self.clubs2)
        self.stockpile.append(self.clubs3)
        self.stockpile.append(self.clubs4)
        self.stockpile.append(self.clubs5)
        self.stockpile.append(self.clubs6)
        self.stockpile.append(self.clubs7)
        self.stockpile.append(self.clubs8)
        self.stockpile.append(self.clubs9)
        self.stockpile.append(self.clubs10)
        self.stockpile.append(self.clubsJ)
        self.stockpile.append(self.clubsQ)
        self.stockpile.append(self.clubsK)

        # Spades Cards
        #self.spades = []
        self.spadesA = Cards(self.win,  stockpile_position, 100, 150, "Spades", 1, "Black")
        self.spades2 = Cards(self.win,  stockpile_position, 100, 150, "Spades", 2, "Black")
        self.spades3 = Cards(self.win,  stockpile_position, 100, 150, "Spades", 3, "Black")
        self.spades4 = Cards(self.win,  stockpile_position, 100, 150, "Spades", 4, "Black")
        self.spades5 = Cards(self.win,  stockpile_position, 100, 150, "Spades", 5, "Black")
        self.spades6 = Cards(self.win,  stockpile_position, 100, 150, "Spades", 6, "Black")
        self.spades7 = Cards(self.win,  stockpile_position, 100, 150, "Spades", 7, "Black")
        self.spades8 = Cards(self.win,  stockpile_position, 100, 150, "Spades", 8, "Black")
        self.spades9 = Cards(self.win,  stockpile_position, 100, 150, "Spades", 9, "Black")
        self.spades10 = Cards(self.win, stockpile_position, 100, 150, "Spades", 10, "Black")
        self.spadesJ = Cards(self.win,  stockpile_position, 100, 150, "Spades", 11, "Black")
        self.spadesQ = Cards(self.win,  stockpile_position, 100, 150, "Spades", 12, "Black")
        self.spadesK = Cards(self.win,  stockpile_position, 100, 150, "Spades", 13, "Black")
        self.stockpile.append(self.spadesA)
        self.stockpile.append(self.spades2)
        self.stockpile.append(self.spades3)
        self.stockpile.append(self.spades4)
        self.stockpile.append(self.spades5)
        self.stockpile.append(self.spades6)
        self.stockpile.append(self.spades7)
        self.stockpile.append(self.spades8)
        self.stockpile.append(self.spades9)
        self.stockpile.append(self.spades10)
        self.stockpile.append(self.spadesJ)
        self.stockpile.append(self.spadesQ)
        self.stockpile.append(self.spadesK)

        """
        # Append cards to deck
        self.deck = []
        self.deck.append(self.hearts)
        self.deck.append(self.diamonds)
        self.deck.append(self.clubs)
        self.deck.append(self.spades)
        """

        # Randomize deck
        random.shuffle(self.stockpile)
        """
        random.shuffle(self.hearts)
        random.shuffle(self.diamonds)
        random.shuffle(self.clubs)
        random.shuffle(self.spades)
        random.shuffle(self.deck)
        """

        # Place 28 cards in a seperate array
        # These cards will be placed in the 7 player columns
        #self.column_cards = []
        #for i in range(4):
        #    for j in range(7):
        #        self.column_cards.append(self.deck[i][j])

        # Place the other 24 cards in a seperate array
        #self.stock_cards = []
        #self.deck.reverse()
        #for i in range(4):
        #    for j in range(6):
        #        self.stock_cards.append(self.deck[i][j])

        self.start_deck(75, 125)


    def start_deck(self, x, y):
        # This function places the 28 column cards across the 7 columns

        #self.stockpile.reverse()

        s = .07 # Constant for sleep function

        sleep(1)
        
        #column 1
        self.stockpile[0].moveCard(x, y)
        sleep(s)
        self.stockpile[0].moveCard(x, y)

        #column 2
        j = 0
        for i in range(1, 3):
            self.stockpile[i].moveCard(x + 75, y)
            sleep(s)
            self.stockpile[i].moveCard(x + 75, y + j)
            j += 10
        
        #column 3
        j = 0
        for i in range(3, 6):
            self.stockpile[i].moveCard(x + 150, y)
            sleep(s)
            self.stockpile[i].moveCard(x + 150, y + j)
            j += 10
        
        #column 4
        j = 0
        for i in range(6, 10):
            self.stockpile[i].moveCard(x + 225, y)
            sleep(s)
            self.stockpile[i].moveCard(x + 225, y + j)
            j += 10
        
        #column 5
        j = 0
        for i in range(10, 15):
            self.stockpile[i].moveCard(x + 300, y)
            sleep(s)
            self.stockpile[i].moveCard(x + 300, y + j)
            j += 10

        #column 6
        j = 0
        for i in range(15, 21):
            self.stockpile[i].moveCard(x + 375, y)
            sleep(s)
            self.stockpile[i].moveCard(x + 375, y + j)
            j += 10

        #column 7
        j = 0
        for i in range(21, 28):
            self.stockpile[i].moveCard(x + 450, y)
            sleep(s)
            self.stockpile[i].moveCard(x + 450, y + j)
            j += 10
        
        sleep(s)
        self.stockpile[0].showFront()
        sleep(s)
        self.stockpile[2].showFront()
        sleep(s)
        self.stockpile[5].showFront()
        sleep(s)
        self.stockpile[9].showFront()
        sleep(s)
        self.stockpile[14].showFront()
        sleep(s)
        self.stockpile[20].showFront()
        sleep(s)
        self.stockpile[27].showFront()
        sleep(s)
        
        

    def StartMenu(self):
        self.win = GraphWin("Solitaire", 500, 300)
        self.win.setBackground("green")

        self.Quit = Button(self.win, Point(350, 100), 120, 50, "Quit Game")
        self.Quit.activate()

        self.Start = Button(self.win, Point(150, 100), 120, 50, "Start Game")
        self.Start.activate()

        q = self.win.getMouse()


        if self.Quit.clicked(q):
         self.win.close()
        """
        elif self.Start.clicked(q):
            self.win.close()
        
            playsound.playsound('poker.mp3', False)
        """

        
            
inter = Solitaire()
