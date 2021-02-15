from graphics      import *
from button        import *
from cards         import *
from time          import *
from random        import *
from playsound     import *
from Card_Movement import *

class Solitaire:

    def __init__(self):
        """
            Sets the Game of Solitary here you will find all the objects for
            the starting of the game.
        """
        self.ST_win = GraphWin("Solitaire", 500, 200)
        self.ST_win.setCoords(0,0,500,200)  #Placed Set Coords for better placing the objects
        self.ST_win.setBackground("green")
        self.Quit = Button(self.ST_win, Point(350, 100), 120, 50, "Quit Game")
        self.Quit.activate()
        self.Start = Button(self.ST_win, Point(150, 100), 120, 50, "Start Game")
        self.Start.activate()
        self.Selection = self.StartMenu() 
        self.Game_Setup()

    def Game_Setup(self):
        
        if self.Selection == "Start":
          self.stockpile = []  
          self.win = GraphWin("Solitaire", 1000, 900)
          self.foundationPiles1 = Button(self.win, Point(525, 700), 100, 150, "Foundation")
          self.foundationPiles2 = Button(self.win, Point(650, 700), 100, 150, "Foundation")
          self.foundationPiles3 = Button(self.win, Point(775, 700), 100, 150, "Foundation")
          self.foundationPiles4 = Button(self.win, Point(900, 700), 100, 150, "Foundation")
          self.Time             = Button(self.win, Point(575, 850), 120, 50 ,       "Time")   #<-- No buttons, just updated text
          self.Score            = Button(self.win, Point(425, 850), 120, 50 ,      "Score")   #<-- No buttons, just updated text
          self.win.setCoords(0,0,1000,900) #Placed Set Coords for better placing the objects
          self.win.setBackground("green")
          self.Time.activate()
          self.Score.activate()
          self.foundationPiles1.activate()
          self.foundationPiles2.activate()
          self.foundationPiles3.activate()
          self.foundationPiles4.activate()
          self.QuitButton = Button(self.win, Point(575, 100), 120, 50, "Quit")
          self.QuitButton.activate()
          
          self.UndoButton = Button(self.win, Point(425, 100), 120, 50, "Undo")
          self.UndoButton.activate()
          self.create_cards()
        else:
          pass

    def button_functions(self):
        Selection=self.win.checkMouse()
        if Selection == None:
            pass
        elif self.QuitButton.clicked(Selection):
            self.win.close()
            self.Selection=self.StartMenu()
            self.Game_Setup()
        elif self.UndoButton.clicked(Selection):  #DON'T CHANGE PLEASE by: Gabriel Roman
            self.UndoButton.Undo_Activate(self.win,Card)
        else:
            self.UndoButton.movement_store(Card,self.win)



    def create_cards(self):
        stockpile_position = Point(100, 700) # Starting position of the entire deck
        colors=["Red","Black"]
        c=0
        types=["Hearts","Diamonds","Clubs","Spades"]
        t=0
        x=0
        #self.hearts = []
        for i in range(52):
          if x < 13:
           Card = Cards(self.win,  stockpile_position, 100, 150, types[t], x+1, colors[c])
           self.stockpile.append(Card)
           x=x+1
          else:
           t=t+1
           x=0
           if t == 2:
               c=c+1
               Card = Cards(self.win,  stockpile_position, 100, 150, types[t], x+1, colors[c])
               self.stockpile.append(Card)
           else:
               Card = Cards(self.win,  stockpile_position, 100, 150, types[t], x+1, colors[c])
               self.stockpile.append(Card)


        # Randomize deck
        
        #shuffle(self.stockpile)  # Revisar

        self.start_cards(0, 250)


    def start_cards(self, x, y):
        # This function places the 28 column cards across the 7 columns

        #self.stockpile.reverse()

        s = 0.07 # Constant for sleep function

        
        
        #column 1
        self.stockpile[0].showFront()
        self.stockpile[0].moveCard_Start(x, y)
        sleep(s)
        
        
        #column 2
        j = 0
        for i in range(1,3):
            if i < 2: 
              self.stockpile[i].moveCard_Start(x + 125, y+j)
              sleep(s)
              j += 20
            else:
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 125, y+j)
              sleep(s)
              
        
        #column 3
        j = 0
        for i in range(3, 6):
            if i < 5: 
              self.stockpile[i].moveCard_Start(x + 250, y+j)
              sleep(s)
              j += 20
            else:
              
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 250, y+j)
              sleep(s)
        
        #column 4
        j = 0
        for i in range(6, 10):
            if i < 9: 
              self.stockpile[i].moveCard_Start(x + 375, y+j)
              sleep(s)
              j += 20
            else:
              
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 375, y+j)
              sleep(s)
        
        #column 5
        j = 0
        for i in range(10, 15):
            if i < 14: 
              self.stockpile[i].moveCard_Start(x + 500, y+j)
              sleep(s)
              j += 20
            else:
              
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 500, y+j)
              sleep(s)

        #column 6
        j = 0
        for i in range(15, 21):
            if i < 20: 
              self.stockpile[i].moveCard_Start(x + 625, y+j)
              sleep(s)
              j += 20
            else:
             
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 625, y+j)
              sleep(s)

        #column 7
        j = 0
        for i in range(21, 28):
            if i < 27: 
              self.stockpile[i].moveCard_Start(x + 750, y+j)
              sleep(s)
              j += 20
            else:
              
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 750, y+j)
              sleep(s)
        

    def StartMenu(self):

        Correct_Selection=False
        #playsound('poker.mp3', False)
        while Correct_Selection == False:  
          Select_B = self.ST_win.checkMouse()
          Selection = "Start"
          if Select_B == None:
              pass
          elif self.Quit.clicked(Select_B):
            Correct_Selection = True
            Selection = "Quit"
            self.ST_win.close()
            return Selection
           
          elif self.Start.clicked(Select_B):
            Correct_Selection = True
            self.ST_win.close()
            return Selection
          else:
            pass
            
        
            
        

        
#if __name__=="__main__":           
Test = Solitaire()
setting=True
while setting:
    Test.button_functions()
