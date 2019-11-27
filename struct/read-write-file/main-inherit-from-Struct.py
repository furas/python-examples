#!/usr/bin/env python3 

# date: 2019.11.27
# 

import struct
from collections import namedtuple

class SP(struct.Struct):

    def __init__(self):
        super().__init__('i20s')
        self.i = 0
        self.s = ''
        
    def read(self, stream):
        buffer = stream.read(self.size)
        data = self.unpack(buffer)
        self.i = data[0]
        self.s = data[1].decode()
        
    def write(self, stream):
        buffer = self.pack(self.i, self.s.encode())
        stream.write(buffer)

class SP:

    def __init__(self):
        self.format = 'i20s'
        self.size = struct.calcsize(self.format)
        self.i = 0
        self.s = ''
        
    def read(self, stream):
        buffer = stream.read(self.size)
        data = struct.unpack(self.format, buffer)
        self.i = data[0]
        self.s = data[1].decode()
        
    def write(self, stream):
        data = (self.i, self.s.encode())
        buffer = struct.pack(self.format, *data)
        stream.write(buffer)
        
        
def main():

  sp = SP()
  
  print('--- OPEN ---')
  
  stream = open("test.bin", 'rb+');  

  # ---
  
  print('--- READ ---')
  
  sp.read(stream)

  print('int:', sp.i) # int
  print('str:', sp.s) # char[20]
  
  # ---
  
  print('--- SEEK ---')
  
  stream.seek(0, 0)
  
  # ---

  print('--- WRITE ---')

  sp.i = 123
  sp.s = "abcdef"

  sp.write(stream)

  # ----
  
  print('--- SEEK ---')
  
  stream.close()

  #input("PAUSE (press ENTER)")

main()
