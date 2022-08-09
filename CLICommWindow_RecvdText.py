from tkinter import *
from tkinter import ttk
import CLICommWindow_Editbar

class CLICommWindow_RecvdText(Frame):
  inst = None
  def __init__(self, aOwner):
    CLICommWindow_RecvdText.inst = self
    self.owner = aOwner
    Frame.__init__(self,self.owner.windowGet())
    self.index = '1.0'
    self.recvdText = Text(self)
    self.recvdText.pack(side=LEFT, fill=BOTH, expand=True)
    self.pack(side=TOP, fill=BOTH, expand=True)
    self.recvdText.configure(state="disabled")

    sb_ = Scrollbar(self)
    self.recvdText.config(yscrollcommand=sb_.set)
    sb_.config(command=self.recvdText.yview)
    sb_.pack(side=RIGHT, fill=BOTH)
    self.createPopupMenu()
    
  def createPopupMenu(self):
    self.popup = Menu(self.owner.windowGet(), tearoff=0)
    self.popup.add_command(label="Copy to clipboard", command=self.doClipboard)
    self.popup.add_command(label="Copy to entry", command=self.doEntry)
    self.popup.add_command(label="Append to entry", command=self.doAppend)
    self.recvdText.bind("<Button-3>", self.doPopup)    

  def doPopup(self, aEvent):
    try:
      if self.recvdText.selection_get():
        try: # display the popup menu
          self.popup.tk_popup(aEvent.x_root, aEvent.y_root, 0)
        finally:  # make sure to release the grab (Tk 8.0a1 only)
          self.popup.grab_release()
    except:
      pass
  
  def nameGet():
    return 'Received Text'
    
  def append(self, aString):
    self.recvdText.configure(state="normal")
    self.recvdText.insert('end', aString)
    self.recvdText.configure(state="disabled")

  def doSearch(aString):
    print("srch recvd")
    self_ = CLICommWindow_RecvdText.inst
    self_.searchStrLen = len(aString)
    self_.recvdText.tag_remove(SEL, '1.0', END)
    index_ = self_.recvdText.search( aString, self_.index, nocase=1, stopindex=END)
    if not index_:
      self_.index = '1.0'
    else:
      lastidx_ = '%s+%dc' % (index_, len(aString))
      self_.recvdText.tag_add(SEL, index_, lastidx_)
      self_.index = lastidx_
      self_.recvdText.tag_config(SEL, foreground='blue')
 
  def doClipboard(self):
    text_ = self.recvdText.selection_get()
    if text_:
      self.owner.windowGet().clipboard_clear()
      self.owner.windowGet().clipboard_append(self.recvdText.selection_get())
    
  def doEntry(self):
    text_ = self.recvdText.selection_get()
    if text_:
      CLICommWindow_Editbar.CLICommWindow_Editbar.set(text_)
    
  def doAppend(self):
    text_ = self.recvdText.selection_get()
    if text_:
      CLICommWindow_Editbar.CLICommWindow_Editbar.append(text_)
    