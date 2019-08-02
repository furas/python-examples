
# First version

- app.py
- top_block_22.py
 
It uses only `time.sleep(0.5)` to play short sound. 

Code originally was splited in two files.

# Thread

- main-thread.py

It uses `Thread` to play sound all time - and change it by recreating thread.

# Lastest

- main-lastest.py

Object already use thread to play sound so this code uses its methods
to start and stop sound. 

It shows 3 methods to change new sound

- deleting and creating new `TopBlock22`

- using lock/unlock and disconnect/connect to recreate `analog.sample_f`

- using `analog.sample_f.set_samling_freq()` (it seems has no clicks when sound changes but I fill there is delay before sound changed after mouse click)

