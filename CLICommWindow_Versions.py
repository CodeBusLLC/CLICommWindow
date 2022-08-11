from tkinter import *
from tkinter import ttk
import serial
from serial.tools.list_ports import comports

class CLICommWindow_Versions(Toplevel):
  def __init__(self, aOwner, aVersions):
    super().__init__()
    self.portSelected = None
    self.title("Versions")
    self.owner = aOwner
    fr = Frame(self)
    # Listbox creation
    self.versions = Listbox(fr, width = 30)
    self.versions.pack(side=TOP, padx=20, pady=20)
    self.versions.insert(END, *aOwner.versions)
    fr.pack()
    
    self.protocol("WM_DELETE_WINDOW", self.doClose)
    self.owner.windowGet().wm_attributes("-disabled", True)
    self.wait_window(self)    

  def doClose(self):
      self.owner.windowGet().wm_attributes("-disabled", False) # IMPORTANT!  
      self.destroy()    
    