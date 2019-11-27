#!/usr/bin/env python3 

# date: 2019.11.27
# 

import struct

struct_format = 'i20s'
struct_length = struct.calcsize(struct_format)

def main():

  print('--- OPEN ---')

  stream = open("test.bin", 'rb+');  

  # ---

  print('--- READ ---')

  buffer = stream.read(struct_length)
  i, s = struct.unpack(struct_format, buffer)

  print('int:', i) # int
  print('str:', s.decode()) # char[20]

  # ---

  print('--- SEEK ---')

  stream.seek(0, 0)

  # ---

  print('--- WRITE ---')

  i = 333
  s = "abcde".encode()

  buffer = struct.pack(struct_format, i, s)
  stream.write(buffer)

  # ---

  print('--- CLOSE ---')

  stream.close()

  #input("PAUSE (press ENTER)")

main()
