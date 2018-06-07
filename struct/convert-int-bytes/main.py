#!/usr/bin/env python3

import struct


number = 2018

data = struct.pack('I', number)

print(data)  # b'\xe2\x07\x00\x00'
print(list(data))  # [226, 7, 0, 0]

# ---------------------------------------------------------------------

data = bytes([226, 7, 0, 0])
data = b'\xe2\x07\x00\x00'
data = b''.join([b'\xe2', b'\x07', b'\x00', b'\x00'])

number = struct.unpack('I', data)[0]  # [0] - first element in tuple

print(number)  # 2018
