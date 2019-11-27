#!/usr/bin/env python3 

# date: 2019.11.27
# 

import struct
from collections import namedtuple

struct_format = 'i20s'
struct_length = struct.calcsize(struct_format)

SP = namedtuple('SP', 'i s')
        
def main():
  print('--- OPEN ---')
  
  stream = open("test.bin", 'rb+');  

  # ---
  
  print('--- READ ---')
  
  buffer = stream.read(struct_length)
  data = struct.unpack(struct_format, buffer)
  sp = SP._make(data) # create tuple 

  print('int:', sp.i) # int
  print('str:', sp.s.decode()) # char[20]
  
  # ---
  
  print('--- SEEK ---')
  
  stream.seek(0, 0)
  
  # ---

  print('--- WRITE ---')

  # tuple can't change value so it needs to create new tuple
  sp = SP(i=123, s="abcdef".encode())

  buffer = struct.pack(struct_format, *sp) # need * to unpack data
  stream.write(buffer)

  # ----
  
  print('--- SEEK ---')
  
  stream.close()

  #input("PAUSE (press ENTER)")

main()
