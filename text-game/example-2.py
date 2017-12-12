rooms = {
    'room1': {
        'description': "Your in a room how to get out...",
    },
    'room2': {
        'description': "This is the second room",
    },
    'room3': {
        'description': "This is the third room",
    },
}

def show_room(name):
    print(rooms[name]['description'])

    star
    looking_forward = False
    looking_backward = False

    while True:
        answer = input().lower()
        if answer == 'exit':
            print("Good Bye")
            return
        if answer == "look forward":
            if not looking_forward:
                print("You are looking forward")
                looking_forward = True
                looking_backward = False
            else:            
                print("You are already looking forward, so what next")
        elif answer == 'look backward':
            if not looking_backward:
                print("You are looking backward")
                looking_forward = False
                looking_backward = True
            else:            
                print("You are already looking backward, so what next")
        elif answer == 'go there':
            if looking_forward:
                return 'room2'
            if looking_backward:
                return 'room3'
            else:
                print('Go where ???')

# --------------------------------

name = 'room1'

while name is not None:
    name = show_room(name)

