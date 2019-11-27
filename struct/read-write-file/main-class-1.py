#!/usr/bin/env python3 

# date: 2019.11.27
# 

import struct

class SP:

    def __init__(self):
        self.format = 'i20s'
        self.length = struct.calcsize(self.format)
        self.i = 0
        self.s = b''

    def pack(self):
        return struct.pack(self.format, self.i, self.s)

    def unpack(self, data):
        self.i, self.s = struct.unpack(self.format, data)

def main():

  sp = SP()

  # ---

  print('--- OPEN ---')

  stream = open("test.bin", 'rb+');  

  # ---

  print('--- READ ---')

  buffer = stream.read(sp.length)
  sp.unpack(buffer)  

  print('int:', sp.i) # int
  print('str:', sp.s.decode()) # char[20]

  # ---

  print('--- SEEK ---')

  stream.seek(0, 0)

  # ---

  print('--- WRITE ---')

  sp.i = 987
  sp.s = "ABCDE".encode()

  buffer = sp.pack()
  stream.write(buffer)

  # ---

  print('--- CLOSE ---')

  stream.close()

  #input("PAUSE (press ENTER)")

main()
