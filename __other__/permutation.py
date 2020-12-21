import itertools

def permut(data):
    data = list(data) # convert string to list

    if len(data) < 2:
        yield data
    else:
        for i, x in enumerate(data):
            for y in permut(data[:i] + data[i+1:]):
                yield [x] + y

data = ['', 'a', 'ab', 'abc', [1,2,3]]

for text in data:    
    print(list(permut(text)))
    print(list(itertools.permutations(text)))
    print('---')
    
