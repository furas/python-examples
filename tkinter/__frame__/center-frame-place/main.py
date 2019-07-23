
# date: 2019.07.23
# https://stackoverflow.com/questions/57151341/is-there-a-way-to-make-the-output-center-itself-in-tkinter/57154709#57154709

import re
import tkinter as tk

# --- functions ---

def sign_in():
    print('hello ' + signin_user.get())

def sign_up():
    # []    A set of characters    "[a-m]"    
    # \    Signals a special sequence (can also be used to escape special characters)    "\d"    
    # .    Any character (except newline character)    "he..o"    
    # ^    Starts with    "^hello"    
    # $    Ends with    "world$"    
    # *    Zero or more occurrences    "aix*"    
    # +    One or more occurrences    "aix+"    
    # {}    Exactly the specified number of occurrences    "al{2}"    
    # |    Either or    "falls|stays"    
    # ()    Capture and group
    regpass = "^[A-Z][\w(!@#$%^&*_+?)+]{8,}$"
    if not (re.search(regpass,reg_password.get())):
         m.configure(text='''->Spaces and empty sets are not allowed.
        \n ->First character should be a capital letter.
        \n ->Password must be greater than 8 character and must contain a special character.''')
    elif (reg_password != reg_cnfpassword):
        m.configure(text='Password and Confirm Password must match')
    else :
        m.configure(text='')

# --- main ---

root = tk.Tk()
root.title('Password Manager')
root.geometry('500x500')

signin_user = tk.StringVar()
signin_password = tk.StringVar()
reg_name = tk.StringVar()
reg_user = tk.StringVar()
reg_password = tk.StringVar()
reg_cnfpassword = tk.StringVar()


f = tk.Frame(root)
f.place(relx=0.5, rely=0.5, anchor='c')

tk.Label(f, text='User Name : ').grid(row=0, column=0, sticky='e')
tk.Entry(f, textvariable=signin_user).grid(row=0, column=1)

tk.Label(f, text='Password : ').grid(row=1, column=0, sticky='e')
tk.Entry(f, textvariable=signin_password).grid(row=1, column=1)

tk.Button(f, text="Sign In", width=10, command=sign_in).grid(row=2, column=0, columnspan=2)
tk.Label(f, text="Sign up", font='Helvetica 18 bold').grid(row=3, column=0, columnspan=2, pady=20)

tk.Label(f, text="Name : ").grid(row=4, column=0, sticky='e')
tk.Entry(f, textvariable=reg_name).grid(row=4, column=1)

tk.Label(f, text="User Name : ").grid(row=5, column=0, sticky='e')
tk.Entry(f, textvariable=reg_user).grid(row=5, column=1)

tk.Label(f, text="Password : ").grid(row=6, column=0, sticky='e')
tk.Entry(f, textvariable=reg_password).grid(row=6, column=1)

tk.Label(f, text="Confirm password : ").grid(row=7, column=0, sticky='e')
tk.Entry(f, textvariable=reg_cnfpassword).grid(row=7, column=1)

m = tk.Message(f, text='Hello World', bg="red")
m.grid(row=8, column=0, columnspan=2, sticky='we')

tk.Button(f, text="Sign Up", width=10, command=sign_up).grid(row=9, column=0, columnspan=2)

root.mainloop()

