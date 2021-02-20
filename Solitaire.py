from graphics      import *
from button        import *
from cards         import *
from time          import *
from random        import *
from pygame        import *              # used only for the song; see lines:

class Solitaire:

    def __init__(self):
        """
            Sets the Game of Solitaire. Here you will find all the objects for
            the start of the game.
        """
        self.ST_win = GraphWin("Solitaire", 500, 300)
        self.ST_win.setCoords(0,0,500,200)  #Placed Set Coords for better placing the objects
        self.ST_win.setBackground("green")
        self.Quit = Button(self.ST_win, Point(350, 100), 100, 25, "Quit Game")
        self.Quit.activate()
        self.Start = Button(self.ST_win, Point(150, 100), 100, 25, "Start Game")
        self.Start.activate()
        self.Rule = Button(self.ST_win, Point(250, 25), 100, 25, "Rules")
        self.Rule.activate()
        self.Selection = self.StartMenu() 
        self.Game_Setup()
        
    def Winner_GI(self):
          self.W_win = GraphWin("Congratulatations", 500, 500)
          self.W_win.setBackground('green')

          comment1 = "WINNER WINNER CHICKEN DINNER"
          comment2 = "Score \t\t\t\t\t Points"
          comment3 =  "Foundation Pile: \t\t\t\t\t", self.total_points
          comment4 = "Time Bonus: \t\t\t\t ", timer_info

          line = "-" * 90
          texts = []
          text1 = Text(Point(250, 70), comment1)
          text2 = Text(Point(250, 260), comment2)
          text3 = Text(Point(250, 280),line )
          text4 = Text(Point(250, 320), comment3)
          text5 = Text(Point(250, 340), comment4)
          texts.append(text1)
          texts.append(text2)
          texts.append(text3)
          texts.append(text4)
          texts.append(text5)

         

          for t in texts:
            t.draw(self.W_win)


    def Game_Setup(self):
        
        if self.Selection == "Start":
          self.stockpile_rectangle = Rectangle(Point(150, 775), Point(50, 625))
          self.current_stockpile_card = 24

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

          self.RuleButton = Button(self.win, Point(80, 50),120, 50, "Help")
          self.RuleButton.activate()

          self.NewGameButton = Button(self.win, Point(220, 50), 120, 50, "Start Over")
          self.NewGameButton.activate()
          
          self.create_cards()

          self.selected_flag = False
          self.selected_card = []
          
        else:
          pass
        
    def button_functions(self):
        Selection=self.win.checkMouse()
        if Selection == None:
            pass

        # elif 50 <= Selection.getX() <= 150 and 625 <= Selection.getY() <= 775:
        #         if self.current_stockpile_card == 51:
        #             self.current_stockpile_card = 0
        #         self.stockpile[self.current_stockpile_card].move_card(Point(300, 700))
        #         self.stockpile[self.current_stockpile_card].showFront()
        #         self.current_stockpile_card += 1 
            

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
        
        elif self.RuleButton.clicked(Selection):
          self.Rules()

        elif self.NewGameButton.clicked(Selection):
          self.New_Game()

        elif self.QuitButton.clicked(Selection):
          self.check_quit()

        else:     # Handle clicks of cards in columns
            #selected_flag = False
            #selected_card = []

            for c in range(52):
                  
                # Handle first card selection
                if self.stockpile[c].card_click(Selection) and not self.selected_flag and not self.stockpile[c].isTopOfChain() and not self.stockpile[0].isPartOfChain():     
                    self.stockpile[c].selected()
                    self.selected_card.append(self.stockpile[c])
                    self.selected_flag = True     

                elif self.stockpile[c].card_click(Selection) and not self.selected_flag and self.stockpile[c].isTopOfChain() and not self.stockpile[0].isPartOfChain():
                    self.stockpile[c].selected()
                    self.selected_card.append(self.stockpile[c])
                    self.selected_flag = True

                elif self.stockpile[c].card_click(Selection) and not self.selected_flag and not self.stockpile[c].isTopOfChain() and self.stockpile[0].isPartOfChain():
                    self.stockpile[c].selected()
                    self.selected_card.append(self.stockpile[c])
                    self.selected_flag = True

                # Handle placement of selected card, and flip of backwards card
                elif self.stockpile[c].card_click(Selection) and self.selected_flag:     

                    # If selected card is clicked again, then deselect it
                    if (self.selected_card[0].getType() == self.stockpile[c].getType() and
                        self.selected_card[0].getNumber() == self.stockpile[c].getNumber()):
                          self.selected_card[0].deselect()
                          self.selected_card.clear()
                          self.selected_flag = False


                    # If selected card is not clicked again, handle placement of selected card
                    elif (self.selected_card[0].getNumber() < self.stockpile[c].getNumber() and
                        self.selected_card[0].getColor() is not self.stockpile[c].getColor()):

                          # If selected card is the top of a chain of cards
                          if self.selected_card[0].isTopOfChain() and not self.selected_card[0].isPartOfChain():
                              self.selected_card[0].move_card(self.stockpile[c].getCenter())
                              last_center = self.selected_card[0].getCenter()
                              for i in self.selected_card[0].chained_tableau_column:
                                  i.move_card(last_center)
                                  last_center = i.getCenter()

                              # Handle excolumn and newcolumn
                              ex_column = self.selected_card[0].getTableau_Column()
                              new_column = self.stockpile[c].getTableau_Column()
                              self.selected_card[0].setTableau_Column(new_column)
                              self.tableau_cards[new_column - 1].append(self.selected_card[0])
                              self.tableau_cards[ex_column - 1].remove(self.selected_card[0])
                              for i in self.selected_card[0].chained_tableau_column:
                                  i.setTableau_Column(new_column)
                                  self.tableau_cards[new_column - 1].append(i)
                                  if self.tableau_cards[ex_column - 1].count(i) is not 0:
                                    self.tableau_cards[ex_column - 1].remove(i)
                              size = -1
                              for i in self.tableau_cards[ex_column - 1]:
                                size += 1
                              if size >= 0 and self.tableau_cards[ex_column - 1][size].getHidden():
                                self.tableau_cards[ex_column - 1][size].showFront()

                              # Handle chains
                              front_cards = 0
                              size = 0
                              chain = []
                              for i in self.tableau_cards[new_column - 1]:
                                size += 1
                                if not i.getHidden():
                                  front_cards += 1
                              if front_cards > 1:     # if there is a chain of front cards
                                self.tableau_cards[new_column - 1][size - front_cards].setTopOfChain()
                                for i in range(1, front_cards):
                                  chain.append(self.tableau_cards[new_column - 1][size - i])
                                  self.tableau_cards[new_column - 1][size - i].setChainFlag(self.tableau_cards[new_column - 1][size - front_cards])
                                chain.reverse()
                                self.tableau_cards[new_column - 1][size - front_cards].setRestOfChain(chain)  
                                                                                                                     
                                                                    
                              self.selected_card[0].deselect()
                              self.selected_card.clear()
                              self.selected_flag = False
                          

                          # Next card selected is part of a chain
                          elif self.selected_card[0].isPartOfChain() and not self.selected_card[0].isTopOfChain():
                              self.selected_card[0].move_card(self.stockpile[c].getCenter())

                              # Handle excolumn and newcolumn
                              ex_column = self.selected_card[0].getTableau_Column()
                              new_column = self.stockpile[c].getTableau_Column()
                              self.selected_card[0].setTableau_Column(new_column)
                              self.tableau_cards[new_column - 1].append(self.selected_card[0])
                              self.tableau_cards[ex_column - 1].remove(self.selected_card[0])
                              size = -1
                              for i in self.tableau_cards[ex_column - 1]:
                                size += 1
                              if size >= 0 and self.tableau_cards[ex_column - 1][size].getHidden():
                                self.tableau_cards[ex_column - 1][size].showFront()

                              # Handle ex chain
                              ex_chain = self.selected_card[0].get_top_of_chain()                              
                              ex_chain.chained_tableau_column.remove(self.selected_card[0])


                              # Handle chains
                              front_cards = 0
                              size = 0
                              chain = []
                              for i in self.tableau_cards[new_column - 1]:
                                size += 1
                                if not i.getHidden():
                                  front_cards += 1
                              if front_cards > 1:     # if there is a chain of front cards
                                self.tableau_cards[new_column - 1][size - front_cards].setTopOfChain()
                                for i in range(1, front_cards):
                                  chain.append(self.tableau_cards[new_column - 1][size - i])
                                  self.tableau_cards[new_column - 1][size - i].setChainFlag(self.tableau_cards[new_column - 1][size - front_cards])
                                chain.reverse()
                                self.tableau_cards[new_column - 1][size - front_cards].setRestOfChain(chain)                                                                                                                                    
                                                            

                              self.selected_card[0].deselect()
                              self.selected_card.clear()
                              self.selected_flag = False
                              


                          # Next card selected is not top of a chain nor part of a chain
                          else:
                              self.selected_card[0].move_card(self.stockpile[c].getCenter())

                              # Handle excolumn and newcolumn
                              ex_column = self.selected_card[0].getTableau_Column()
                              new_column = self.stockpile[c].getTableau_Column()
                              self.selected_card[0].setTableau_Column(new_column)
                              self.tableau_cards[new_column - 1].append(self.selected_card[0])
                              self.tableau_cards[ex_column - 1].remove(self.selected_card[0])
                              size = -1
                              for i in self.tableau_cards[ex_column - 1]:
                                size += 1
                              if size >= 0 and self.tableau_cards[ex_column - 1][size].getHidden():
                                self.tableau_cards[ex_column - 1][size].showFront()

                              # Handle chains
                              #new_column = self.selected_card[0].getTableau_Column()
                              front_cards = 0
                              size = 0
                              chain = []
                              for i in self.tableau_cards[new_column - 1]:
                                size += 1
                                if not i.getHidden():
                                  front_cards += 1
                              if front_cards > 1:     # if there is a chain of front cards
                                #num_of_tops = 0
                                #array_of_tops = []
                                # for i in range(1 + 1, front_cards + 1):
                                #   self.tableau_cards[new_column - 1][size - i].setTopOfChain()
                                #   array_of_tops.append(self.tableau_cards[new_column - 1][size - i])
                                #   num_of_tops += 1
                                # if num_of_tops > 1:
                                #   for i in range(1, front_cards):
                                #     for j in range(1, num_of_tops):
                                #       chain[i - 1].append(self.tableau_cards[new_column - 1][size - i])
                                #       self.tableau_cards[new_column - 1][size - i].setChainFlag(self.tableau_cards[new_column - 1][size - front_cards])
                                #       if i is not j:
                                #         chain[i].append(self.tableau_cards[new_column - 1][size - j])
                                #         self.tableau_cards[new_column - 1][size - j].setChainFlag(self.tableau_cards[new_column - 1][size - num_of_tops])


                                    
                                self.tableau_cards[new_column - 1][size - front_cards].setTopOfChain()
                                for i in range(1, front_cards):
                                  chain.append(self.tableau_cards[new_column - 1][size - i])
                                  self.tableau_cards[new_column - 1][size - i].setChainFlag(self.tableau_cards[new_column - 1][size - front_cards])
                                chain.reverse()
                                self.tableau_cards[new_column - 1][size - front_cards].setRestOfChain(chain)                                                                                                                                    


                              self.selected_card[0].deselect()
                              self.selected_card.clear()
                              self.selected_flag = False


                #if 
              
              
            

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

        self.tableau_cards = []
        self.column1 = []
        self.tableau_cards.append(self.column1)
        self.column2 = []
        self.tableau_cards.append(self.column2)
        self.column3 = []
        self.tableau_cards.append(self.column3)
        self.column4 = []
        self.tableau_cards.append(self.column4)
        self.column5 = []
        self.tableau_cards.append(self.column5)
        self.column6 = []
        self.tableau_cards.append(self.column6)
        self.column7 = []
        self.tableau_cards.append(self.column7)


        s = 0.07 # Constant for sleep function
        
        #column 1
        self.stockpile[0].showFront()
        self.stockpile[0].moveCard_Start(x, y)
        self.stockpile[0].setTableau_Column(1)
        self.tableau_cards[0].append(self.stockpile[0])
        sleep(s)
        
        
        #column 2
        j = 0
        for i in range(1,3):
            if i < 2: 
              self.stockpile[i].moveCard_Start(x + 125, y+j)
              self.stockpile[i].setTableau_Column(2)
              self.tableau_cards[1].append(self.stockpile[i])
              sleep(s)
              j += 20
            else:
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 125, y+j)
              self.stockpile[i].setTableau_Column(2)
              self.tableau_cards[1].append(self.stockpile[i])
              sleep(s)
              
        
        #column 3
        j = 0
        for i in range(3, 6):
            if i < 5: 
              self.stockpile[i].moveCard_Start(x + 250, y+j)
              self.stockpile[i].setTableau_Column(3)
              self.tableau_cards[2].append(self.stockpile[i])
              sleep(s)
              j += 20
            else:
              
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 250, y+j)
              self.stockpile[i].setTableau_Column(3)
              self.tableau_cards[2].append(self.stockpile[i])
              sleep(s)
        
        #column 4
        j = 0
        for i in range(6, 10):
            if i < 9: 
              self.stockpile[i].moveCard_Start(x + 375, y+j)
              self.stockpile[i].setTableau_Column(4)
              self.tableau_cards[3].append(self.stockpile[i])
              sleep(s)
              j += 20
            else:
              
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 375, y+j)
              self.stockpile[i].setTableau_Column(4)
              self.tableau_cards[3].append(self.stockpile[i])
              sleep(s)
        
        #column 5
        j = 0
        for i in range(10, 15):
            if i < 14: 
              self.stockpile[i].moveCard_Start(x + 500, y+j)
              self.stockpile[i].setTableau_Column(5)
              self.tableau_cards[4].append(self.stockpile[i])
              sleep(s)
              j += 20
            else:
              
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 500, y+j)
              self.stockpile[i].setTableau_Column(5)
              self.tableau_cards[4].append(self.stockpile[i])
              sleep(s)

        #column 6
        j = 0
        for i in range(15, 21):
            if i < 20: 
              self.stockpile[i].moveCard_Start(x + 625, y+j)
              self.stockpile[i].setTableau_Column(6)
              self.tableau_cards[5].append(self.stockpile[i])
              sleep(s)
              j += 20
            else:
             
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 625, y+j)
              self.stockpile[i].setTableau_Column(6)
              self.tableau_cards[5].append(self.stockpile[i])
              sleep(s)

        #column 7
        j = 0
        for i in range(21, 28):
            if i < 27: 
              self.stockpile[i].moveCard_Start(x + 750, y+j)
              self.stockpile[i].setTableau_Column(7)
              self.tableau_cards[6].append(self.stockpile[i])
              sleep(s)
              j += 20
            else:
              
              self.stockpile[i].showFront()
              self.stockpile[i].moveCard_Start(x + 750, y+j)
              self.stockpile[i].setTableau_Column(7)
              self.tableau_cards[6].append(self.stockpile[i])
              sleep(s)
        

    def StartMenu(self):
        Correct_Selection=False
        while Correct_Selection == False:  
          Select_B = self.ST_win.checkMouse()
          if Select_B == None:
              pass
          elif self.Quit.clicked(Select_B):
              exit(Solitaire)
              self.ST_win.close()
              self.win.close()
          elif self.Start.clicked(Select_B):
            Correct_Selection = True
            Selection = "Start"
            self.ST_win.close()

            mixer.init() #the only instance we use pygame 
            mixer.music.load('poker.wav') #the only instance we use pygame
            mixer.music.play(-1) #the only instance we use pygame 

            return Selection

          elif self.Rule.clicked(Select_B):
              Correct_Selection = False
              self.Rules()
              self.StartMenu()
              Selection = "Start"
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
      if self.total_points >= 40 :
          self.Winner_GI()

      self.Score_number.undraw()
      self.Score_number = Text(Point(350, 850), self.total_points)
      self.Score_number.setTextColor("black")
      self.Score_number.draw(self.win)
    # end Score()
    
    def Rules(self):
          self.R_Win = GraphWin("Rules of Solitaire", 500, 500) # Graphical Window of the Rules
          self.R_Win.setBackground('green')

          bullets = []
          bullet1= Circle(Point(40, 25), 3)
          bullets.append(bullet1)
          bullet2 = Circle(Point(40, 175), 3)
          bullets.append(bullet2)
          for b in bullets:
                b.setFill("black")
                b.draw(self.R_Win)

          bulletpoint1 = "The first objective is to release and play into position\n certain cards to build up each foundation, in sequence \nand in suit, from the ace through the king. \nThe ultimate objective is to build the whole pack onto the \nfoundations, and if that can be done, \nthe Solitaire game is won."
          bulletpoint2 = "The rank of cards in Solitaire games is: \nK (high), Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A (low)."

          line = "-" * 90
          row1 = "Score \t\t\t\t\t Points"
          row2 = "Points per Foundation Pile piled \t\t\t + 10"
          row3 = "Columns Piled \t\t\t\t\t  + 1"
          row4 = "Time Bonus \t\t\t\t + (may vary)"

          texts= []
          text1 = Text(Point(250, 70), bulletpoint1)
          text2 = Text(Point(250, 180), bulletpoint2)

          text_row1 = Text(Point(250, 260), row1)
          text_line = Text(Point(250, 280), line)
          text_row2 = Text(Point(250, 300), row2)
          text_row3 = Text(Point(250, 320), row3)
          text_row4 = Text(Point(250, 340), row4)

          texts.append(text1)
          texts.append(text2)
          texts.append(text_line)
          texts.append(text_row1)
          texts.append(text_row2)
          texts.append(text_row3)
          texts.append(text_row4)

          for t in texts:
            t.draw(self.R_Win)

          back = Button(self.R_Win, Point(475, 480), 40, 30, "Exit")
          back.activate()

          pt = self.R_Win.getMouse()
          if back.clicked(pt):
            self.R_Win.close()

          while not back.clicked(pt):
            pt = self.R_Win.getMouse()
            if back.clicked(pt):
                self.R_Win.close()


    def New_Game(self):
        self.N_win = GraphWin("Quit Game", 500, 200)
        self.N_win.setCoords(0,0,500,200)  #Placed Set Coords for better placing the objects
        self.N_win.setBackground("green")

        

        msg = "Are you sure you want to quit this game?"
        msg2 = "You'll lose all your progress!"
        display_msg = Text(Point(250, 175), msg)
        display_msg2 = Text(Point(250, 150), msg2)
        display_msg.setTextColor('black')
        display_msg2.setTextColor('black')
        display_msg.draw(self.N_win)
        display_msg2.draw(self.N_win)

        self.yes = Button(self.N_win, Point(200, 50), 50, 50, "Yes")
        self.yes.activate()
        self.no = Button(self.N_win, Point(300, 50), 50, 50, "No")
        self.no.activate()

        p = self.N_win.getMouse()
        if self.yes.clicked(p):
          self.N_win.close()
          self.ST_win.close()
          self.win.close()
          self.__init__()
        elif self.no.clicked(p):
          self.N_win.close()
        while not self.yes.clicked(p) and not self.no.clicked(p):
          p = self.N_win.getMouse()
          if self.yes.clicked(p):
            self.N_win.close()
            self.ST_win.close()
            self.win.close()
            self.__init__()
          elif self.no.clicked(p):
            self.N_win.close()
              


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
