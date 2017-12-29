#!/usr/bin/env python

from easygui_timerbox import timerbox

timerbox('Time to the end of the World', 'Countdown', time=5)

result = timerbox('Last change to save the World', 'Countdown', choices=['BUM!', 'Save the World'], time=5)

if result == 'BUM!':
    timerbox('Time to BUM !!!', 'Countdown', choices=['OK'], time=5)
else:
    timerbox('You saved the World !', 'Countdown', choices=['OK'], time=5)
