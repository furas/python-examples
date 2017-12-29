
`timerbox` based on `EasyGui 0.96`.

It has new argument `time=seconds` and it closes messagebox after that time.

You need only `easygui_timerbox.py` without original `easygui`

    from easygui_timerbox import timerbox
    
    timerbox('Time to the end of the World', 'Countdown', time=5)
    
---

In `example.py` (you can see the same if you run `python easygui_timerbox.py`)


    timerbox('Time to the end of the World', 'Countdown', time=5)


![#1](images/screenshot-1.png?raw=true)   

    result = timerbox('Last change to save the World', 'Countdown', choices=['BUM!', 'Save the World'], time=5)

![#1](images/screenshot-2.png?raw=true)   

    timerbox('Time to BUM !!!', 'Countdown', choices=['OK'], time=5)

![#1](images/screenshot-3.png?raw=true)   

    timerbox('You saved the World !', 'Countdown', choices=['OK'], time=5)

![#1](images/screenshot-4.png?raw=true)   
