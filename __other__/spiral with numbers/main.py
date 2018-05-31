import math

__author__ = 'Bartłomiej "furas" Burek'

__all__ = ['spiral', 'fake']


def test_sizes(numbers=26):
    '''Show matrix size and start position for 1..numbers'''

    for value in range(1, numbers+1):
        size = math.ceil(math.sqrt(value))
        print('[TEST] numbers:', value, 'size:', size)


def test_starts(value=6):
    '''Show start position for sizes 1..value'''
    

    for size in range(1, value):
        center = math.floor((size-1) / 2)
        x = center
        y = (size - 1) - center # flip up-down
        print('[TEST] size:', size, 'start:', x, y, '(x,y)')


def spiral(numbers, remove_empty_rows=True, DEBUG=False):

    if DEBUG:
        print('[DEBUG] numbers:', numbers)

    # size of square matrix (to keep all values)
    size = math.ceil(math.sqrt(numbers))
    if DEBUG:
        print('[DEBUG] matrix size:', size)

    data = [[''] * size for _ in range(size)]
    #print('data:', data)

    # start positon for value `1` 
    center = math.floor((size-1) / 2)
    x = center
    y = (size - 1) - center # flip up-down

    if DEBUG:
        print('[DEBUG] start:', x, y, '(x,y)') 

    # (move_y,move_x) for "right", "up", "left", "down"
    moves = [(0,1), (-1,0), (0,-1), (1,0)]
    
    # every move has to be repeated: 1,1,2,2,3,3,4,4,5,5,etc.
    # so it will be [1,1], later [1,2], later [2,2], later [2,3], etc.
    repeats = [1, 1]

    # put `1` in matrix in starting position
    value = 1
    data[y][x] = value

    # put other values
    while value < numbers:
        # get direction from beginning of list
        move_y, move_x = moves.pop(0)
        # get how many times to move in this direction - get it from beginning of list
        repeat = repeats.pop(0)
        
        for _ in range(repeat):
            # get next value
            value += 1
            # move to new place
            y += move_y 
            x += move_x
            # put value in matrix
            data[y][x] = value
            
            # for some values you have to make less repeates at the end
            if value >= numbers:
                break
                
        # put repeat+1 at the end of list
        repeats.append(repeat+1)        
        # put direction at the end of list
        moves.append((move_y, move_x))    

    # added later: it removes empty rows. 
    # Code passes test without filter too.
    # Test needs `list()` to get correct data from `filter()`
    if remove_empty_rows:
        data = list(filter(any, data))
    
    return data


def fake(numbers):
    '''Check testing function for fake results'''
    return list(range(1, numbers+1))


if __name__ == '__main__':

    test_sizes(26)
    print('---')
    test_starts(6)
    print('---')

    for value in [5, 8, 10]:
        matrix = spiral(value, True)
    
        for row in matrix:
            print(row)
    
