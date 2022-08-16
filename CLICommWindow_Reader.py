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
    self.port = None
    self.disconnectRequest = False
    self.ser = serial.Serial()
    self.ser.baudrate = 115200
    self.ser.timeout = .1
    self.toSend = None
    self.start()
    
  def run(self):
    while CLICommWindow_Reader.doRun:
      if self.disconnectRequest:
        self.ser.close()
        self.disconnectRequest = False
        
      if self.ser and self.ser.is_open:
        if self.toSend:
          self.ser.write( self.toSend.encode(encoding='utf-8') )
          self.toSend = None
        line_ = self.ser.read(128)
        if line_:
          lineDecoded_ = line_.decode(encoding='utf-8')
          #print(lineDecoded_)
          self.owner.processText(lineDecoded_)
    if self.ser:
      self.ser.close()
      self.ser = None
    return
  
  def stop(self):
    CLICommWindow_Reader.doRun = False
  
  def openConnection(self, aPort):
    self.ser.port = aPort
    self.ser.open()
    if self.ser.is_open:
      self.port = aPort
      self.owner.connected(True, self.port)
  
  def disconnect(self):
    self.disconnectRequest = True
    self.owner.connected(False, self.port)

  def reconnect(self):
    self.ser.open()
    if self.ser.is_open:
      self.owner.connected(True, self.port)
    
  def send(self, aString):
    self.toSend = aString
    