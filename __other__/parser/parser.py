import sys

#print sys.argv[0], len( sys.argv )
if len(sys.argv) > 1:

    with open(sys.argv[1], 'r') as f_in:

        result = 0

        for line in f_in:
            data = line.strip().split()
#            print('data:', data)
            if data[0] == "+":
                result += float(data[1])
            elif data[0] == "-":
                result -= float(data[1])
            elif data[0] == "=":
                print("RESULT:", result)
                result = 0
            else:
                print('unknow:', data)
