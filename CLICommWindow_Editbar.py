from tkinter import *
from tkinter import ttk
import CLICommWindow_Reader

class CLICommWindow_Editbar(Frame):
  inst = None
  def __init__(self, aOwner):
    Frame.__init__(self, aOwner.windowGet())
    CLICommWindow_Editbar.inst = self
    self.history = []
    self.entry = ttk.Combobox(self, state=DISABLED)
    self.btnEnter = Button(self, text="Send", command=self.doSend, state=DISABLED)
    self.btnEnter.pack(side=LEFT, padx=4)
    self.entry.pack(side=RIGHT, padx=4, fill=X, expand=True)
    self.pack(side=TOP, fill=X)
  
  def enable(self, aEnable):
    stateNew_ = NORMAL
    if not aEnable:
      stateNew_ = DISABLED
    self.entry['state'] = stateNew_
    self.btnEnter['state'] = stateNew_
      
  def doSend(self):
    entry_ = self.entry.get()
    if entry_ in self.history:
      self.history.remove(entry_)
      self.history.insert(0, entry_)
    else:
      self.history.append(entry_)
      
    self.entry['values'] = self.history
    self.entry.delete(0,len(entry_))
    CLICommWindow_Reader.CLICommWindow_Reader.inst.send(entry_)
    
  def set(aString):
    CLICommWindow_Editbar.inst.entry.set(aString)
    
  def append(aString):
    CLICommWindow_Editbar.inst.entry.set(CLICommWindow_Editbar.inst.entry.get() + aString)
    