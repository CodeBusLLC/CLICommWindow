from tkinter import *
from tkinter import ttk
import CLICommWindow_Reader
import CLICommWindow_Connect
import CLICommWindow_Treeview

class CLICommWindow_Menu:
  def __init__(self, aOwner):
    self.owner = aOwner
    menubar = Menu(aOwner.windowGet())
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Connect", command=self.doConnect)
    filemenu.add_command(label="Disconnect", command=self.doDisconnect)
    filemenu.add_command(label="Reconnect", command=aOwner.donothing)
    filemenu.add_command(label="Save as...", command=aOwner.donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=aOwner.donothing)
    menubar.add_cascade(label="File", menu=filemenu)
    
    viewmenu = Menu(menubar, tearoff=0)
    viewmenu.add_command(label="Collapse", command=self.doCollapse)
    viewmenu.add_command(label="Expand", command=self.doExpand)
    menubar.add_cascade(label="View", menu=viewmenu)
    
    aOwner.windowGet().config(menu=menubar)
    
  def doConnect(self):
    cd = CLICommWindow_Connect.CLICommWindow_Connect(self.owner)
    port_ = cd.portSelectedGet()
    if port_:
      print("Connecting to %s" % (port_))
      CLICommWindow_Reader.CLICommWindow_Reader.inst.openConnection(port_)
      self.owner.windowGet().title("%s - %s" % (self.owner.titleGet(), port_))

  def doDisconnect(self):
    pass
    
  def doCollapse(self):
    CLICommWindow_Treeview.CLICommWindow_Treeview.collapse()
    
  def doExpand(self):
    CLICommWindow_Treeview.CLICommWindow_Treeview.expand()
