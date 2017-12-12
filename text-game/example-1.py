def first_room():
    print("Your in a room how to get out...")

    looking_forward = False
    looking_backward = False

    while True:
        question = input().lower()
        if question == "look forward":
            if not looking_forward:
                print("You are looking forward")
                looking_forward = True
                looking_backward = False
            else:            
                print("You are already looking forward, so what next")
        elif question == 'look backward':
            if not looking_backward:
                print("You are looking backward")
                looking_forward = False
                looking_backward = True
            else:            
                print("You are already looking backward, so what next")
        elif question == 'go there':
            if looking_forward:
                return second_room
            if looking_backward:
                return third_room
            else:
                print('Go where ???')
                
                
def second_room():
    print("This is the second room")


def third_room():
    print("This is the third room") 

# --------------------------------

next_room = first_room

while next_room is not None:
    next_room = next_room()

print("Good Bye")
