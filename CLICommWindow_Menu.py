from tkinter import *
from tkinter import ttk
import CLICommWindow_Reader
import CLICommWindow_Connect
import CLICommWindow_Treeview
import CLICommWindow_RecvdText
import CLICommWindow_Search

class CLICommWindow_Menu:
  def __init__(self, aOwner):
    self.owner = aOwner
    menubar = Menu(aOwner.windowGet())
    self.filemenu = Menu(menubar, tearoff=0)
    self.filemenu.add_command(label="Connect", command=self.doConnect)
    self.filemenu.add_command(label="Disconnect", command=self.doDisconnect, state=DISABLED)
    self.filemenu.add_command(label="Reconnect", command=self.doReconnect, state=DISABLED)
    self.filemenu.add_separator()
    self.filemenu.add_command(label="Exit", command=self.owner.doClose)
    menubar.add_cascade(label="File", menu=self.filemenu)
    
    viewmenu = Menu(menubar, tearoff=0)
    viewmenu.add_command(label="Collapse", command=self.doCollapse)
    viewmenu.add_command(label="Expand", command=self.doExpand)
    menubar.add_cascade(label="View", menu=viewmenu)
    
    searchmenu = Menu(menubar, tearoff=0)
    searchmenu.add_command(label="Element Tree", command=self.doSearchTree)
    searchmenu.add_command(label="Received Text", command=self.doSearchRecvd)
    menubar.add_cascade(label="Search", menu=searchmenu)

    aOwner.windowGet().config(menu=menubar)

  def connected(self, aConnected):
    if aConnected:
      self.filemenu.entryconfig('Connect', state=DISABLED)
      self.filemenu.entryconfig('Disconnect', state=NORMAL)
      self.filemenu.entryconfig('Reconnect', state=DISABLED)
    else:
      self.filemenu.entryconfig('Connect', state=NORMAL)
      self.filemenu.entryconfig('Disconnect', state=DISABLED)
      self.filemenu.entryconfig('Reconnect', state=NORMAL)

    
  def doConnect(self):
    cd = CLICommWindow_Connect.CLICommWindow_Connect(self.owner)
    port_ = cd.portSelectedGet()
    if port_:
      print("Connecting to %s" % (port_))
      CLICommWindow_Reader.CLICommWindow_Reader.inst.openConnection(port_)

  def doDisconnect(self):
    CLICommWindow_Reader.CLICommWindow_Reader.inst.disconnect()
  
  def doReconnect(self):
    CLICommWindow_Reader.CLICommWindow_Reader.inst.reconnect()
    
  def doCollapse(self):
    CLICommWindow_Treeview.CLICommWindow_Treeview.collapse()
    
  def doExpand(self):
    CLICommWindow_Treeview.CLICommWindow_Treeview.expand()

  def doSearchTree(self):
    dlgSearch_ = CLICommWindow_Search.CLICommWindow_Search(self, CLICommWindow_Treeview.CLICommWindow_Treeview)
    pass
    
  def doSearchRecvd(self):
    dlgSearch_ = CLICommWindow_Search.CLICommWindow_Search(self, CLICommWindow_RecvdText.CLICommWindow_RecvdText)
    pass
 