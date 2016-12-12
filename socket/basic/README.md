# Version #1

It is basic version which sends and receives one short message.

# Version #2 

It uses `while True` to receive long message using small buffer.

    SIZE = 10
    
    data = b'' # empty byte 

    while True:
        chain = s.recv(SIZE)
        print('[TEST] chain:', chain)
        data += chain

        if len(chain) < SIZE:
            break

    text = data.decode('utf-8') # decode bytes to string

    print(text)

# Version #3

See: [Simple Protocol](../simple-protocol)

It first sends message's length as `int` converted to `4-bytes`. 

    length_bytes = struct.pack('!i', length_int)

# Version #4

It uses threads to handle many clients at the same time.

Python doc: [threading](https://docs.python.org/3/library/threading.html)

Other examples: [Thread](../../thread)

