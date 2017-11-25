rom Tkinter import *
import ttk

class MainWindow(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("ProgressBar example")
        #self.master.minsize(400, 100)
        self.grid(sticky=E+W+N+S)

        #-----

        self.var_ind = IntVar(self)

        self.pbar_ind = ttk.Progressbar(self, orient="horizontal", length=400, mode="indeterminate", variable=self.var_ind, maximum=100)
        self.pbar_ind.grid(row=0, column=0, pady=2, padx=2, sticky=E+W+N+S, columnspan=3)

        Label(self, text="indeterminate").grid(row=1, column=0, pady=2, padx=2, sticky=E+W+N+S)

        self.lab_ind_var = Label(self, text="VAR:")
        self.lab_ind_var.grid(row=1, column=1, pady=2, padx=2, sticky=E+W+N+S)

        self.lab_ind_max = Label(self, text="MAX:")
        self.lab_ind_max.grid(row=1, column=2, pady=2, padx=2, sticky=E+W+N+S)

        #-----

        self.var_det = IntVar(self)

        self.pbar_det = ttk.Progressbar(self, orient="horizontal", length=400, mode="determinate", variable=self.var_det, maximum=100)
        self.pbar_det.grid(row=2, column=0, pady=2, padx=2, sticky=E+W+N+S, columnspan=3)

        Label(self, text="determinate").grid(row=3, column=0, pady=2, padx=2, sticky=E+W+N+S)

        self.lab_det_var = Label(self, text="VAR:")
        self.lab_det_var.grid(row=3, column=1, pady=2, padx=2, sticky=E+W+N+S)

        self.lab_det_max = Label(self, text="MAX:")
        self.lab_det_max.grid(row=3, column=2, pady=2, padx=2, sticky=E+W+N+S)

        #-----

        Label(self, text="ANIMATION:").grid(row=4, column=0, pady=2, padx=2, sticky=E+W+N+S)

        Button(self, text='START', command=self.animation_start).grid(row=4, column=1, pady=2, padx=2, sticky=E+W+N+S)
        Button(self, text='STOP', command=self.animation_stop).grid(row=4, column=2, pady=2, padx=2, sticky=E+W+N+S)

        #-----

        Label(self, text="SET:").grid(row=5, column=0, pady=2, padx=2, sticky=E+W+N+S)

        Button(self, text='BEGIN', command=self.set_begin).grid(row=5, column=1, pady=2, padx=2, sticky=E+W+N+S)
        Button(self, text='END', command=self.set_end).grid(row=5, column=2, pady=2, padx=2, sticky=E+W+N+S)

        #-----

        Label(self, text="SET:").grid(row=6, column=0, pady=2, padx=2, sticky=E+W+N+S)

        Button(self, text='23', command=lambda:self.set(23)).grid(row=6, column=1, pady=2, padx=2, sticky=E+W+N+S)
        Button(self, text='77', command=lambda:self.set(77)).grid(row=6, column=2, pady=2, padx=2, sticky=E+W+N+S)

        #-----

        Label(self, text="SET:").grid(row=7, column=0, pady=2, padx=2, sticky=E+W+N+S)

        Button(self, text='+23', command=lambda:self.set_plus(23)).grid(row=7, column=1, pady=2, padx=2, sticky=E+W+N+S)
        Button(self, text='-77', command=lambda:self.set_plus(-77)).grid(row=7, column=2, pady=2, padx=2, sticky=E+W+N+S)

        #-----

        Label(self, text="STEP:").grid(row=8, column=0, pady=2, padx=2, sticky=E+W+N+S)

        Button(self, text='+1', command=lambda:self.step(1)).grid(row=8, column=1, pady=2, padx=2, sticky=E+W+N+S)
        Button(self, text='-10', command=lambda:self.step(-10)).grid(row=8, column=2, pady=2, padx=2, sticky=E+W+N+S)

        #-----

        Label(self, text="MAX:").grid(row=9, column=0, pady=2, padx=2, sticky=E+W+N+S)

        Button(self, text='100', command=lambda:self.max(100)).grid(row=9, column=1, pady=2, padx=2, sticky=E+W+N+S)
        Button(self, text='200', command=lambda:self.max(200)).grid(row=9, column=2, pady=2, padx=2, sticky=E+W+N+S)

        #-----

        self.update_labels_after = False
        self.update_labels()

    #-----          

    def animation_start(self):
        self.update_labels_after = True

        self.pbar_ind.start() # .start(1)
        self.pbar_det.start() # .start(1)

        self.update_labels()

    def animation_stop(self):
        self.update_labels_after = False

        self.pbar_ind.stop()
        self.pbar_det.stop()

        self.update_labels()

    #-----          

    def set_begin(self):
        self.var_ind.set( 0 )
        self.var_det.set( 0 )

        self.update_labels()

    def set_end(self):
        self.var_ind.set( self.pbar_ind.cget('maximum') )
        self.var_det.set( self.pbar_det.cget('maximum') )

        self.update_labels()

    #-----          

    def set(self, val):
        self.var_ind.set( val )
        self.var_det.set( val )

        self.update_labels()

    #-----          

    def set_plus(self, val):
        self.var_ind.set( self.var_ind.get() + val )
        self.var_det.set( self.var_det.get() + val )

        self.update_labels()

    #-----          

    def step(self, val=1):
        self.pbar_ind.step(val) # .step()
        self.pbar_det.step(val) # .step()

        self.update_labels()

    #-----          

    def max(self, val=1):
        self.pbar_ind.config(maximum=val)
        self.pbar_det.config(maximum=val)

        self.update_labels()

    #-----          

    def update_labels(self):

        self.lab_ind_var.config(text='VAR: %d' % (self.var_ind.get()))
        self.lab_ind_max.config(text='MAX: %d' % (self.pbar_ind.cget('maximum')))

        self.lab_det_var.config(text='VAR: %d' % (self.var_det.get()))
        self.lab_det_max.config(text='MAX: %d' % (self.pbar_det.cget('maximum')))

        if self.update_labels_after:
            self.after(50, self.update_labels)

if __name__=="__main__":
   MainWindow().mainloop()
