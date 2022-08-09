import threading
from tkinter import *
from tkinter import ttk

import CLICommWindow_Menu
import CLICommWindow_Treeview
import CLICommWindow_Editbar
import CLICommWindow_RecvdText
import CLICommWindow_Reader

class Application(Tk):
  strTitle = "CommWindow V0.1"
  def __init__(self):
    Tk.__init__(self)
    self.window = self
    self.title(Application.strTitle)
    self.minsize(width=800, height=800)
    self.geometry("500x500")
    gui = GUI(self)
    self.protocol("WM_DELETE_WINDOW", gui.doClose)    
    self.window.mainloop()
    
class GUI():
  def __init__(self, aWindow):
    self.window = aWindow
    m = CLICommWindow_Menu.CLICommWindow_Menu(self)
    self.tree = CLICommWindow_Treeview.CLICommWindow_Treeview(self)
    self.editbar = CLICommWindow_Editbar.CLICommWindow_Editbar(self)
    self.recvdText = CLICommWindow_RecvdText.CLICommWindow_RecvdText(self)
    self.reader = CLICommWindow_Reader.CLICommWindow_Reader(self)

  def donothing():
      pass

  def windowGet(self):
    return self.window
    
  def doClose(self):
    self.reader.stop()
    self.window.destroy()
        
  def processText(self, aLine):
    self.recvdText.append(aLine)

  def titleGet(self):
    return Application.strTitle
    
app = Application()
