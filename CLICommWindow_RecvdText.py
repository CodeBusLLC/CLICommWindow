from tkinter import *
from tkinter import ttk

class CLICommWindow_RecvdText(Frame):
  inst = None
  def __init__(self, aOwner):
    CLICommWindow_RecvdText.inst = self
    Frame.__init__(self,aOwner.windowGet())
    self.recvdText = Text(self)
    self.recvdText.pack(side=LEFT, fill=BOTH, expand=True)
    self.pack(side=TOP, fill=BOTH, expand=True)
    self.recvdText.configure(state="disabled")

    sb_ = Scrollbar(self)
    self.recvdText.config(yscrollcommand=sb_.set)
    sb_.config(command=self.recvdText.yview)
    sb_.pack(side=RIGHT, fill=BOTH)    
    
  def append(self, aString):
    self.recvdText.configure(state="normal")
    self.recvdText.insert('end', aString)
    self.recvdText.configure(state="disabled")

  def doSearch(aString):
    print("srch recvd")