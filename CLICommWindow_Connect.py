from tkinter import *
from tkinter import ttk
import serial
from serial.tools.list_ports import comports

class CLICommWindow_Connect(Toplevel):
  def __init__(self, aOwner):
    super().__init__()
    self.portSelected = None
    self.title("Connect")
    self.owner = aOwner
    fr = Frame(self)
    l = Label(fr, text="Please select a port and click Connect")
    l.pack(pady=10)
    # Combobox creation
    self.cbPorts = ttk.Combobox(fr, width = 50)
    portlist = comports()
    plist = []
    for p in portlist:
      plist.append("%s (%s)" % (p.name, p.description))
    self.cbPorts['values'] = plist
    self.cbPorts.pack()
    self.btnOk = Button(fr, text="Connect", command=self.doPortSelected)
    self.btnOk.pack(pady=10)
    fr.pack()
    self.cbPorts.focus_set()
       
    self.protocol("WM_DELETE_WINDOW", self.doClose)
    self.owner.windowGet().wm_attributes("-disabled", True)
    self.wait_window(self)    

  def doClose(self):
      self.owner.windowGet().wm_attributes("-disabled", False) # IMPORTANT!  
      self.destroy()
      
  def doPortSelected(self):
    #print(self.cbPorts.get())
    self.portSelected = self.cbPorts.get().split('(')[0]
    #print(self.portSelected)
    self.doClose()
  
  def portSelectedGet(self):
    return self.portSelected
    
    