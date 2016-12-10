# Version #1

Basic version which sends and receives short message.

# Version #2 

It uses `while True` to receive long message using small buffer.

# Version #3

See: ../simple-protocol

It first sends message's length as `int` converted to `4-bytes`. 

     length_bytes = struct.pack('!i', length_int)
