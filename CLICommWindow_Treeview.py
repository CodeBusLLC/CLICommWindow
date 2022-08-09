from tkinter import *
from tkinter import ttk
import xml.etree.ElementTree as ET
import yaml
import CLICommWindow_Reader
import CLICommWindow_Editbar

class CLICommWindow_Treeview(Frame):
  inst = None
  def __init__(self, aOwner):
    CLICommWindow_Treeview.inst = self
    self.owner = aOwner
    Frame.__init__(self,aOwner.windowGet())
    self.keyItem = None
    self.searchItem = None

    s = ttk.Style()
    s.theme_use('clam')
    s.configure("Treeview.Heading", font=("Calibri",12,'bold'), background='light gray')
    s.configure("Treeview", background="ivory", fieldbackground="ivory", foreground="black")

    columns_=( "Category", "Group", "Element", "Help")
    colWidth_=( 100, 120, 160, 350 )
    tv = ttk.Treeview( self, columns=columns_, show='tree headings', 
                       height=10, selectmode="browse"
                     )
    self.tv = tv
    tv.pack(side=LEFT, fill=X, expand=True)

    tv.heading("#0", text='')
    tv.column("#0", minwidth=20, width=20, stretch=NO)

    stretch_ = NO
    for col_ in range(0, len(columns_)):
      if col_ == 3:
        stretch_ = YES
      tv.column(columns_[col_], width=colWidth_[col_], stretch=stretch_)
      tv.heading(columns_[col_], text=columns_[col_])
    
    tv.bind("<Button-3>", self.doPopup)
    self.createPopupMenu()
    
    tv.bind("<Double-1>", self.OnDoubleClick)
    tv.bind("<Key>", self.OnKey)
    
    sb_ = Scrollbar(self)
    tv.config(yscrollcommand=sb_.set)
    sb_.config(command=tv.yview)
    sb_.pack(side=RIGHT, fill=BOTH)

    self.pack(side=TOP, fill=X)
    
    self.loadTreeYaml()

  def nameGet():
    return 'Element Tree'
    
  def loadTreeYaml(self):
    tv = self.tv  
    with open('elements.yaml', 'r') as file:
      ydata_ = yaml.full_load(file)
      #print(ydata_)
      print(ydata_['Version'])
      for category_ in ydata_['Categories']:
        #print(category_['name'])
        categoryValue_ = category_['value']
        parent_ = tv.insert('', "end", text="", values=(category_['name'], "", "", category_['help']), open=True)
        for element_ in category_['Elements']:
          #print(element_)
          #print( "%s %s" % (element_['name'], element_['value']) )
          help_ = ''
          if 'Help' in element_:
            help_ = element_['Help']
          tv.insert(parent_, "end", text="%s %s" % (categoryValue_, element_['value']), values=("", "", element_['name'], help_), open=True)
        if 'Group' in category_:
          for group_ in category_['Group']:
            help_ = ''
            if 'Help' in group_:
              help_ = group_['Help']
            parent1_ = tv.insert(parent_, "end", text="", values=("", group_['name'], "", help_), open=True)
            for element_ in group_['Elements']:
              #print(element_)
            #print( "%s %s" % (element_['name'], element_['value']) )
              help_ = ''
              if 'Help' in element_:
                help_ = element_['Help']
              tv.insert(parent1_, "end", text="%s %s" % (categoryValue_, element_['value']), values=("", "", element_['name'], help_), open=True)

  def loadTreeXML(self):
    tv = self.tv  
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

  def OnKey(self, aEvent):
    if aEvent.char != '':
      found_ = False
      children_ = self.tv.get_children();
      if self.keyItem != None:
        index_ = self.keyItem + 1
      else:
        index_ = 0
      for i_ in range( index_, len(children_)):
        child_ = children_[i_]
        item_ = self.tv.item(child_)
        if aEvent.char in item_['values'][0]:
          self.tv.focus(child_)
          self.tv.selection_set((child_))
          self.keyItem = i_
          found_ = True
          break 
      if not found_:
        self.keyItem = None      

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
  
  def _searchChildren(self, aIndex, aItem, aString):
    found_ = False
    children_ = self.tv.get_children(aItem);
    for i_ in range( aIndex, len(children_)):
      child_ = children_[i_]
      item_ = self.tv.item(child_)
      if aString in item_['values']:
        self.tv.focus(child_)
        self.tv.selection_set((child_))
        self.searchItem = i_
        return True
      found_ = self._searchChildren(0, child_, aString)
      if found_:
        break
    return found_
        
  def doSearch(aString):
    print("srch tree")
    found_ = False
    self_ = CLICommWindow_Treeview.inst
    tv_ = CLICommWindow_Treeview.inst.tv
    if self_.searchItem != None:
      index_ = self_.searchItem + 1
    else:
      index_ = 0
    found_ = CLICommWindow_Treeview._searchChildren(self_, index_, None, aString)
    if not found_:
      self_.searchItem = None      
    