

# Spiral 

![#1](images/big_spiral.jpg?raw=true)   

## Challange 

Created by [Mark Geyzer](https://www.facebook.com/Mark.Geyzer)

Date: 2018.05.31


The goal of the exercise - create a function that receives an integer number and builds a spiral of numbers - up to the provided number, like in the uppermost picture below

The function output may be:

- list of lists
    
    [[17, 16, 15, 14, 13],
    [18, 5, 4, 3, 12],
    [19, 6, 1, 2, 11, 28],
    [20, 7, 8, 9, 10, 27],
    [21, 22, 23, 24, 25, 26]]

- "flattened" spiral - `(5, 4, 3, 6, 1, 2, 7, 8)`

- simple string output

    ![#1](images/right_image.jpg?raw=true)   

- fancy string output

    ![#1](images/left_image.jpg?raw=true)   

The test harness for function testing is available at [https://repl.it/@volvano63/NumericSpiralTestHarness](https://repl.it/@volvano63/NumericSpiralTestHarness)

The link to collected solutions will be posted in the near future on [this post on Facebook](https://www.facebook.com/groups/python.programmers/permalink/2260989837252153/) in group "Python Programming Language" 

Good luck! I hope you'll enjoy the challenge

---

## Info

I add few examples more to testing code and put in `test.py`.

It imports function(s) from `main.py` 

- `spiral()` - it generate correct resulsts. 
- `fake()` - it generate normal list to checks testing code for fake results.

You can run directly `main.py` to see some results without tests.

### `spiral(numbers, remove_empty=True, DEBUG=False)`

It genearate square matrix (list of list) like this

    
    [[5, 4, 3],
     ['', 1, 2]] 


or with empty rows to keep square size 3x3

    
    [[5, 4, 3],
     ['', 1, 2],
     ['', '', '']]
