from graphics      import *
from button        import *
from cards         import *
from time          import *
from random        import *
from pygame        import *

class Solitaire:

    def __init__(self):
        """
            Sets the Game of Solitaire. Here you will find all the objects for
            the start of the game.
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
          #self.Time             = Button(self.win, Point(575, 850), 120, 50 ,       "Time")   #<-- No buttons, just updated text

          # Draw timer labels
          self.timeLabel1 = Text(Point(640, 850), '0')
          self.dots = Text(Point(650, 850), ':')
          self.timeLabel2 = Text(Point(660, 850), '0')
          self.timeLabel3 = Text(Point(670, 850), '0')
          self.timeLabel1.setTextColor('black')
          self.dots.setTextColor('black')
          self.timeLabel2.setTextColor('black')
          self.timeLabel3.setTextColor('black')
          self.timeLabel1.draw(self.win)
          self.dots.draw(self.win)
          self.timeLabel2.draw(self.win)
          self.timeLabel3.draw(self.win)

          # Draw score labels
          self.Score_label = Text(Point(350, 875), 'Score')
          self.Score_number = Text(Point(350, 850), '0')
          self.Score_label.setTextColor("black")
          self.Score_number.setTextColor("black")
          self.Score_label.draw(self.win)
          self.Score_number.draw(self.win)
          self.total_points = 0     # Initialize self.total_points


          #self.Score = Button(self.win, Point(425, 850), 120, 50 ,      "Score")   #<-- No buttons, just updated text
          self.win.setCoords(0,0,1000,900) #Placed Set Coords for better placing the objects
          self.win.setBackground("green")
          #self.Time.activate()
          #self.Score.activate()
          self.foundationPiles1.activate()
          self.foundationPiles2.activate()
          self.foundationPiles3.activate()
          self.foundationPiles4.activate()
          self.QuitButton = Button(self.win, Point(925, 850), 120, 50, "Quit")
          self.QuitButton.activate()
          
          self.UndoButton = Button(self.win, Point(800, 850), 120, 50, "Undo")
          self.UndoButton.activate()
          
          self.create_cards()
          
        else:
          pass
        
    def button_functions(self):
        Selection=self.win.checkMouse()
        if Selection == None:
            pass

        elif self.foundationPiles1.clicked(Selection):
          self.Score(10)
        elif self.foundationPiles2.clicked(Selection):
          self.Score(10)
        elif self.foundationPiles3.clicked(Selection):
          self.Score(10)
        elif self.foundationPiles4.clicked(Selection):
          self.Score(10)

        elif self.QuitButton.clicked(Selection):
            self.check_quit()

        # elif self.UndoButton.clicked(Selection):  #DON'T CHANGE PLEASE by: Gabriel Roman
        #     self.UndoButton.Undo_Activate(self.win,Card)
        # else:
        #     self.UndoButton.movement_store(Card,self.win)

    def check_quit(self):
        self.Q_win = GraphWin("Quit Game", 500, 200)
        self.Q_win.setCoords(0,0,500,200)  #Placed Set Coords for better placing the objects
        self.Q_win.setBackground("green")

        msg = "Are you sure you want to quit this game?"
        msg2 = "You'll lose all your progress!"
        display_msg = Text(Point(250, 175), msg)
        display_msg2 = Text(Point(250, 150), msg2)
        display_msg.setTextColor('black')
        display_msg2.setTextColor('black')
        display_msg.draw(self.Q_win)
        display_msg2.draw(self.Q_win)

        self.yes = Button(self.Q_win, Point(200, 50), 50, 50, "Yes")
        self.yes.activate()
        self.no = Button(self.Q_win, Point(300, 50), 50, 50, "No")
        self.no.activate()

        p = self.Q_win.getMouse()
        if self.yes.clicked(p):
          exit(Solitaire)
        elif self.no.clicked(p):
          self.Q_win.close()
        while not self.yes.clicked(p) and not self.no.clicked(p):
          p = self.Q_win.getMouse()
          if self.yes.clicked(p):
            exit(Solitaire)
          elif self.no.clicked(p):
            self.Q_win.close()

    def create_cards(self):
        stockpile_position = Point(100, 700) # Starting position of the entire deck
        colors = ["Red","Black"]
        c = 0                                                    # counter for card color
        types = ["Hearts","Diamonds","Clubs","Spades"]
        t = 0                                                    # counter for card type
        x = 0                                                    # counter for card number
        
        for i in range(52):
          if x < 13:
           Card = Cards(self.win,  stockpile_position, 100, 150, types[t], x+1, colors[c])
           self.stockpile.append(Card)
           x += 1
          else:
           t += 1
           x = 0
           if t == 2:
               c += 1
               Card = Cards(self.win,  stockpile_position, 100, 150, types[t], x+1, colors[c])
               self.stockpile.append(Card)
               x += 1
           else:
               Card = Cards(self.win,  stockpile_position, 100, 150, types[t], x+1, colors[c])
               self.stockpile.append(Card)
               x += 1

        # Randomize deck
        shuffle(self.stockpile)

        # Place cards in backward position
        for i in range(52):
            self.stockpile[i].showBack()

        # Call start_cards() function
        self.start_cards(0, 250)

    def start_cards(self, x, y):
        # This function places the 28 column cards across the 7 columns

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
        while Correct_Selection == False:  
          Select_B = self.ST_win.checkMouse()
          if Select_B == None:
              pass
          elif self.Quit.clicked(Select_B):
              exit(Solitaire)
          elif self.Start.clicked(Select_B):
            Correct_Selection = True
            Selection = "Start"
            self.ST_win.close()

            mixer.init()
            mixer.music.load('poker.wav')
            mixer.music.play(-1)

            return Selection
          else:
            pass

    
    def timer(self, gameTimer):
        if gameTimer[1] < 59:
          gameTimer[1] += 1
          if gameTimer[1] <= 9:
            self.timeLabel3.undraw()
            self.timeLabel3 = Text(Point(670, 850), gameTimer[1])
            self.timeLabel3.setTextColor('black')
            self.timeLabel3.draw(self.win)
            self.less_than_ten = True
          elif gameTimer[1] > 9:
            if self.less_than_ten:
              self.timeLabel3.undraw()
              self.less_than_ten = False

            self.timeLabel2.undraw()
            self.timeLabel2 = Text(Point(665, 850), gameTimer[1])
            self.timeLabel2.setTextColor('black')
            self.timeLabel2.draw(self.win)
        
        elif gameTimer[1] == 59:
          gameTimer[1] = 0
          gameTimer[0] += 1
          self.timeLabel1.undraw()

          if gameTimer[0] < 9:
            self.timeLabel1 = Text(Point(640, 850), gameTimer[0])
          else:
            self.timeLabel1 = Text(Point(635, 850), gameTimer[0])

          self.timeLabel1.setTextColor('black')
          self.timeLabel1.draw(self.win)

          self.timeLabel2.undraw()
          self.timeLabel2 = Text(Point(660, 850), 0)
          self.timeLabel3 = Text(Point(670, 850), 0)
          self.timeLabel2.setTextColor('black')
          self.timeLabel3.setTextColor('black')
          self.timeLabel2.draw(self.win)
          self.timeLabel3.draw(self.win)
              
        return gameTimer


    def Score(self, points):
      """
      traer una carta al foundation pile = 10pts
      traer una carta del foundation pile a las columnas = -10pts
      llevar una carta del stockpile a las columnas = 5pts
      carta de columna se vira boca arriba = 5pts
      undo = - la ultima cantidad de puntos que se anadio
      puntos bono por tiempo = 700,000 / total game time in seconds (rounded up)
      """

      self.total_points += points

      self.Score_number.undraw()
      self.Score_number = Text(Point(350, 850), self.total_points)
      self.Score_number.setTextColor("black")
      self.Score_number.draw(self.win)
    # end Score()
          


timer_info = []
seconds = 0
minutes = 0
timer_info.append(minutes)
timer_info.append(seconds)

#if __name__=="__main__":           
Test = Solitaire()
setting = True
while setting:
    Test.button_functions()
    sleep(1)
    timer_info = Test.timer(timer_info)
