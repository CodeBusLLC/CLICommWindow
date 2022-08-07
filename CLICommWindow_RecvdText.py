from tkinter import *
from tkinter import ttk

class CLICommWindow_RecvdText(Frame):
  def __init__(self, aOwner):
    #fr = Frame( )
    Frame.__init__(self,aOwner.windowGet())
    self.recvdText = Text(self)
    self.recvdText.pack(side=LEFT, fill=BOTH, expand=True)
    self.pack(side=TOP, fill=BOTH, expand=True)
    self.recvdText.configure(state="disabled")
    
  def append(self, aString):
    self.recvdText.configure(state="normal")
    self.recvdText.insert('end', aString)
    self.recvdText.configure(state="disabled")
    pass
