from Displays import *
from Button import *
import time


class Counter:
  
  def__init__(self):
    print("Counter:constructor")
    self._number = 0
    self._display = LCDDisplay(sda=20,scl=21,i2cid=0)
    self._greenButton = Button(16, "increase", buttonhandler=self, location)
    self._redButton = Button(17, "reset", buttonhandler=self, lowactrion)
    
  def increment(self):
    print("Counter:incrementing")
    self._number = self._number + 1
    
  def reset(self):
    print("Counter:reset")
    self._number = 0
    
  def buttonPressed(self, name):
    if name == "increase":
      slef.increment()
    elif name == "reset":
      self.reset()
      
  def buttonReleased(self, name):
    pass
  
  def show(self):
    while True:
             self._display.showNumber(self._number)
             time.sleep(0,5)
