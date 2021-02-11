from graphics import *
from cards import *

class Card_Movement(Cards):
  
  """This class is based on how the game will move the cards from
     all the GUI. It contains when the card can be moved, where can it stay,
     when it returns to the place it was before or accept the place the user
     put it in.
  """
  def __init__(self):
    super().__init__()
    self.Card_Mov=Point(0,0)
    self.MOVE=0
    self.cardSL1=Rectangle(Point(500,400),Point(600,600)) #Eliminate after test and add conditions or merge with field program or comment it for future change or testing
    self.cardSL1.setFill("white")                         #Eliminate after test and add conditions or merge with field program or comment it for future change or testing
    self.cardSL1.setOutline("black")                      #Eliminate after test and add conditions or merge with field program or comment it for future change or testing
    self.cardSL1.draw(self.Window)                        #Eliminate after test and add conditions or merge with field program or comment it for future change or testing
    self.cardSL2=Rectangle(Point(300,400),Point(400,600)) #Eliminate after test and add conditions or merge with field program or comment it for future change or testing
    self.cardSL2.setFill("white")                         #Eliminate after test and add conditions or merge with field program or comment it for future change or testing
    self.cardSL2.setOutline("black")                      #Eliminate after test and add conditions or merge with field program or comment it for future change or testing
    self.cardSL2.draw(self.Window)                        #Eliminate after test and add conditions or merge with field program or comment it for future change or testing
  
    self.card.draw(self.Window)


    
  def Card_Move(self,undo):
    
    """Movement of the card"""
    undo.Undo_Activate(self.Window,self.card)
    self.Card_Mov=self.Window.checkMouse()
    Condition,SL=self.Conditions() 
    if self.Card_Mov == None:
      pass
    elif self.Card_Mov.getX() >= self.card.getP1().getX() and self.Card_Mov.getY()>= self.card.getP1().getY() and self.Card_Mov.getX() <= self.card.getP2().getX() and self.Card_Mov.getY() <= self.card.getP2().getY() and self.MOVE==0:  
      self.card.undraw()
      self.card.setOutline("yellow")
      self.card.setWidth(5)
      self.card.draw(self.Window)
      self.MOVE=1
      
    elif self.MOVE==1:
      
      if Condition == True:
       if SL == 1:
         undo.movement_store(self.card,self.Window)
         self.Card_Mov=self.cardSL1.getCenter()
         self.card.move((self.Card_Mov.getX()-self.card.getCenter().getX()),(self.Card_Mov.getY()-self.card.getCenter().getY()))
         self.card.undraw()
         self.card.setOutline("black")
         self.card.setWidth(1)
         self.card.draw(self.Window)
         self.MOVE=0
       elif SL == 2:
         undo.movement_store(self.card,self.Window)
         self.Card_Mov=self.cardSL2.getCenter()
         self.card.move((self.Card_Mov.getX()-self.card.getCenter().getX()),(self.Card_Mov.getY()-self.card.getCenter().getY()))
         self.card.undraw()
         self.card.setOutline("black")
         self.card.setWidth(1)
         self.card.draw(self.Window)
         self.MOVE=0
       else:
         self.card.move(0,0)
         self.card.undraw()
         self.card.setOutline("black")
         self.card.setWidth(1)
         self.card.draw(self.Window)
         self.MOVE=0
      else:
        Message=Text(Point(400,200),"Sorry, you can only move the card to a rack which has the correct card color \nor to finish a pack")
        Message.setFace("times roman")
        Message.setSize(16)
        Message.draw(self.Window)
        i=0
       
        while i < 1000000:
        #waiting time to delete message
          M_out=self.Window.checkMouse()
          if M_out != None:
            Message.undraw()
            i=1000000
          elif i==1000000:
            Message.undraw()
          else:
             i=i+1
    else:
       
       Message=Text(Point(400,200),"Select the card to move.")
       Message.setFace("times roman")
       Message.setSize(16)
       Message.draw(self.Window)
       i=0
       
       while i < 1000000:
         #waiting time to delete message
         
         M_out=self.Window.checkMouse()
         if M_out != None:
           Message.undraw()
           i=1000000
         elif i==1000000:
           Message.undraw()
         else:
           i=i+1
       

  def Conditions(self):
    """ Conditions for movement
    """
    if self.Card_Mov == None:
       return False,0  
    elif self.Card_Mov.getX() >= self.cardSL1.getP1().getX() and self.Card_Mov.getY()>= self.cardSL1.getP1().getY() and self.Card_Mov.getX() <= self.cardSL1.getP2().getX() and self.Card_Mov.getY() <= self.cardSL1.getP2().getY():
       return True,1
    elif self.Card_Mov.getX() >= self.cardSL2.getP1().getX() and self.Card_Mov.getY()>= self.cardSL2.getP1().getY() and self.Card_Mov.getX() <= self.cardSL2.getP2().getX() and self.Card_Mov.getY() <= self.cardSL2.getP2().getY():
       return True,2
    else:
       return False,0

      
  def getWindow(self):
     """
         it returns the atribute window.
     """
     return self.Window




      
class Undo_Botton:

  
  def __init__ (self,Window):
    
    self.Button=Rectangle(Point(300,250),Point(500,300))
    self.Button.setFill("white")
    self.Button.draw(Window)
    self.Label=Text(self.Button.getCenter(),"Undo")
    self.Label.setFill("gray")
    self.Label.draw(Window)
    self.Label_set=1
    self.moves=[]
    self.move_size=len(self.moves)

    
  def movement_store(self,Card,Window):
    
    
    if self.move_size == 10:
      
      del self.moves[0]
      self.moves.append(Card.getCenter())
      
    else:
      
      self.moves.append(Card.getCenter())
      self.move_size=len(self.moves)
      self.Undo_set(Window)

  def Undo_Activate(self,Window,Card):
    
      if self.move_size == 0:
        
        pass
      
      else:
        Condition=Window.checkMouse()
        
        if Condition == None:
          
          pass
        
        elif Condition.getX() >= self.Button.getP1().getX() and Condition.getX() <= self.Button.getP2().getX() and Condition.getY() >= self.Button.getP1().getY() and Condition.getY() <= self.Button.getP2().getY():
          
           Card.move((self.moves[self.move_size-1].getX()-Card.getCenter().getX()),(self.moves[self.move_size-1].getY()-Card.getCenter().getY()))
           del self.moves[(self.move_size-1)]
           self.move_size=len(self.moves)
           self.Undo_set(Window)

        else:
           pass
  
  def Undo_set(self,Window):
     
     
     if self.move_size == 0 and self.Label_set == 0:
        
        self.Label.undraw()
        self.Label.setFill("gray")
        self.Label.draw(Window)
        self.Label_set = 1
        
     elif self.Label_set == 1 and self.move_size > 0:
        
        self.Label.undraw()
        self.Label.setFill("black")
        self.Label.draw(Window)
        self.Label_set=0
        
     else:
       
        pass
      

if __name__ == "__main__": 
      
  Test  = Card_Movement()
  Test2 = Undo_Botton(Test.Window)
  x="on"
  while  x == "on":
  
  
    Test.Card_Move(Test2)
  
    off=Test.Window.checkKey()
    if off == "":
      pass
    else:
      x="off"

    
  Test.Window.close()
    
    
