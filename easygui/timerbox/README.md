
`timerbox` based on `EasyGui 0.96`.

It has new argument `time=seconds` and it closes messagebox after that time.

---

In `example.py`


    timerbox('Time to the end of the World', 'Countdown', time=5)


![#1](images/screenshot-1.png?raw=true)   

    result = timerbox('Last change to save the World', 'Countdown', choices=['BUM!', 'Save the World'], time=5)

![#1](images/screenshot-2.png?raw=true)   

    timerbox('Time to BUM !!!', 'Countdown', choices=['OK'], time=5)

![#1](images/screenshot-3.png?raw=true)   

    timerbox('You saved the World !', 'Countdown', choices=['OK'], time=5)

![#1](images/screenshot-4.png?raw=true)   
