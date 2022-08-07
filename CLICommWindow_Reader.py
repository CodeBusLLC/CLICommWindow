import threading
import time
import serial

class CLICommWindow_Reader(threading.Thread):
  doRun = True
  inst = None
  
  def __init__(self, aOwner):
    super(CLICommWindow_Reader,self).__init__()
    CLICommWindow_Reader.inst = self
    self.owner = aOwner
    self.ser = None
    self.toSend = None
    self.start()
    
  def run(self):
    while CLICommWindow_Reader.doRun:
      if self.ser and self.ser.is_open:
        if self.toSend:
          self.ser.write( self.toSend.encode(encoding='utf-8') )
          self.toSend = None
        line_ = self.ser.read(128)
        if line_:
          lineDecoded_ = line_.decode(encoding='utf-8')
          #print(lineDecoded_)
          self.owner.processText(line_)
    if self.ser:
      self.ser.close()
      self.ser = None
    return
  
  def stop(self):
    CLICommWindow_Reader.doRun = False
  
  def openConnection(self, aPort):
    self.ser = serial.Serial(aPort, 115200, timeout=.1)
    print(self.ser.is_open)
    self.ser.write(b'hello')
    
  def send(self, aString):
    self.toSend = aString