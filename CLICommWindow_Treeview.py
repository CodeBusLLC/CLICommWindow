from tkinter import *
from tkinter import ttk
import xml.etree.ElementTree as ET
import CLICommWindow_Reader
import CLICommWindow_Editbar

class CLICommWindow_Treeview(Frame):
  inst = None
  def __init__(self, aOwner):
    CLICommWindow_Treeview.inst = self
    self.owner = aOwner
    Frame.__init__(self,aOwner.windowGet())
    tv = ttk.Treeview( self, columns=( "Category", "Element", "Help"), show='tree headings', 
                       height=5, selectmode="browse"
                     )
    self.tv = tv
    tv.pack(side=LEFT, fill=X, expand=True)
    self.pack(side=TOP, fill=X)

    tv.heading("#0", text='')
    tv.column("#0", minwidth=20, width=30, stretch=NO)
    tv.heading("Category", text='Category')
    tv.column("Category", width=100, stretch=NO)
    tv.heading("Element", text='Element')
    tv.column("Element", width=100, stretch=NO)
    tv.heading("Help", text='Help')
    tv.column("Help", width=350, stretch=NO)
    
    tv.bind("<Button-3>", self.doPopup)
    self.createPopupMenu()
    
    tv.bind("<Double-1>", self.OnDoubleClick)
    
    #c = tv.insert('', "end", text="0", values=("Show" ), open=True)
    #tv.insert(c, "end", text="0", values=("", "System"))
    
    dataTree_ = ET.parse('elements.xml')
    root_ = dataTree_.getroot()
    for child_ in root_:
      if 'Version' == child_.tag:
        print(child_.get('value'))
      else:
        #print(child_.attrib)
        help_ = child_.get('help')
        if help_ is None:
          help_ = ''
        parent_ = tv.insert('', "end", text="", values=(child_.get('name'), "", help_), open=True)
        for subchild_ in child_:
          help_ = subchild_.find('Help') # notice capital 'H'
          if help_ is None:
            help_ = ''
          else:
            help_ = help_.text.strip()
          tv.insert(parent_, "end", text="%s %s" % (child_.get('value'), subchild_.get('value')), values=("", subchild_.get('name'), help_), open=True)
  
  def createPopupMenu(self):
    self.popup = Menu(self.owner.windowGet(), tearoff=0)
    self.popup.add_command(label="Send", command=self.doSend)
    
  def doPopup(self, aEvent):
    self.selection = self.tv.identify_row(aEvent.y)
    if self.tv.parent(self.selection):
      try: # display the popup menu
        self.popup.tk_popup(aEvent.x_root, aEvent.y_root, 0)
      finally:  # make sure to release the grab (Tk 8.0a1 only)
        self.popup.grab_release()
      
  def doSend(self):
    text = self.tv.item(self.selection)['text']
    parent = self.tv.parent(self.selection)
    textParent = self.tv.item(parent)['text']
    toSend_ = "%s %s" % (textParent, text)
    #print( toSend_ )
    CLICommWindow_Reader.CLICommWindow_Reader.inst.send(toSend_)
    
  def OnDoubleClick(self, aEvent):
    item = self.tv.selection()[0]
    #print("you clicked on", self.tv.item(item,"text"))
    CLICommWindow_Editbar.CLICommWindow_Editbar.set( self.tv.item(item,"text") )

  def collapse():
    tv_ = CLICommWindow_Treeview.inst.tv
    for i_ in tv_.get_children():
      if tv_.parent(i_) == '':
        tv_.item(i_, open=False)

  def expand():
    tv_ = CLICommWindow_Treeview.inst.tv
    for i_ in tv_.get_children():
      if tv_.parent(i_) == '':
        tv_.item(i_, open=True)
  