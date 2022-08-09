from tkinter import *
from tkinter import ttk

class CLICommWindow_Search(Toplevel):
  history = []
  def __init__(self, aOwner, aTarget):
    super().__init__()
    self.target = aTarget
    self.portSelected = None
    self.title("Search: " + aTarget.nameGet())
    self.owner = aOwner
    fr = Frame(self)
    l = Label(fr, text="Please enter the string to search for")
    l.pack()
    # Combobox creation
    self.cbSearch = ttk.Combobox(fr, width = 50)
    self.cbSearch['values'] = CLICommWindow_Search.history
    self.cbSearch.pack()
    self.btnOk = Button(fr, text="Search", command=self.doSearch)
    self.btnOk.pack()
    fr.pack()
       
  def doSearch(self):
    str_ = self.cbSearch.get()
    if str not in CLICommWindow_Search.history:
      CLICommWindow_Search.history.append(str_)
    self.target.doSearch(str_)