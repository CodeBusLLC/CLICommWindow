# CLICommWindow
Python GUI application using tkinter pack layout manager. The application is for simple CLI manipulation. By simple no more than 3 tiers. The CLI commands are presented via a Treeview consisting of columns "Category", "Group", "Element" and "Help". Categories are the top tier, Group allow for grouping Elements of a similar nature. 
The Treeview is populated using a yaml file, although the code is set up to import from XML (does not support Groups yet). The "File" menu supports operations for connecting, disconnecting and reconnecting. The purpose of reconnecting is to that once connected reconnection to the same port does require re-selecting the port.
Treeview mouse operations:
The select mode is browse (single selection).
Right mouse button will present a popup menu with 'Send' which directly sends the command to the connected device
Double clicking will populate the Entry field with the command to send, this allows modification of the base command. This is used for "set" operations where dynamic parameters need to be supplied.
Received Text mouse operations:
If test is selected, right mouse button will present a popup menu with 'Copy to clipboard', 'Copy to entry' and 'Append to entry'

Design
Each field (Treeview, Send btn and Entry, Received Text) reside in their own Class derived from Frame.
The main window acts as an MVC Controller for some operation. While others are class-to-class operations with each class having an instance variable.
