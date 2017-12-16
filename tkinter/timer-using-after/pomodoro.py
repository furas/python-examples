import tkinter as tk

class Timer:
    
    def __init__(self, master):
        self.master = master

        master.title("Pomodoro Timer")

        self.state = False
        self.pause = False
        
        self.mins = 25
        self.secs = 0
            
        self.display = tk.Label(master, text="00 : 00")
        self.display.grid(row=0, column=0, columnspan=2, ipady=10)

        button = tk.Button(master, text="Start", bg="Green", fg="White", activebackground="Light Green", command=self.start)
        button.grid(row=1, column=0, ipady=10)

        button = tk.Button(master, text="Pause", bg="Dark Red", fg="White", activebackground="Red", command=self.pause)
        button.grid(row=1, column=1, ipady=10)

    def countdown(self):
        if self.state == True:
            
            if (self.mins == 0) and (self.secs == 0):
                self.display.config(text="Done!")
                self.state = False
            else:
                self.display.config(text="%02d : %02d" % (self.mins, self.secs))

                if self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    self.secs -= 1
                    
                self.master.after(1000, self.countdown)

    def start(self):
        if self.state == False:
            self.state = True
            self.mins = 25
            self.secs = 0
            self.countdown()

    def pause(self):
        if self.state == True:
            self.state = False

root = tk.Tk()
Timer(root)
root.mainloop()
