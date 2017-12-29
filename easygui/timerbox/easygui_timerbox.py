"""
@version: 0.96(2010-08-29)

@note:
ABOUT EASYGUI

EasyGui provides an easy-to-use interface for simple GUI interaction
with a user.  It does not require the programmer to know anything about
tkinter, frames, widgets, callbacks or lambda.  All GUI interactions are
invoked by simple function calls that return results.

@note:
WARNING about using EasyGui with IDLE

You may encounter problems using IDLE to run programs that use EasyGui. Try it
and find out.  EasyGui is a collection of Tkinter routines that run their own
event loops.  IDLE is also a Tkinter application, with its own event loop.  The
two may conflict, with unpredictable results. If you find that you have
problems, try running your EasyGui program outside of IDLE.

Note that EasyGui requires Tk release 8.0 or greater.

@note:
LICENSE INFORMATION

EasyGui version 0.96

Copyright (c) 2010, Stephen Raymond Ferg

All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer. 
    
    2. Redistributions in binary form must reproduce the above copyright notice,
       this list of conditions and the following disclaimer in the documentation and/or
       other materials provided with the distribution. 
    
    3. The name of the author may not be used to endorse or promote products derived
       from this software without specific prior written permission. 

THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

@note:
ABOUT THE EASYGUI LICENSE

This license is what is generally known as the "modified BSD license",
aka "revised BSD", "new BSD", "3-clause BSD".
See http://www.opensource.org/licenses/bsd-license.php

This license is GPL-compatible.
See http://en.wikipedia.org/wiki/License_compatibility
See http://www.gnu.org/licenses/license-list.html#GPLCompatibleLicenses

The BSD License is less restrictive than GPL.
It allows software released under the license to be incorporated into proprietary products. 
Works based on the software may be released under a proprietary license or as closed source software.
http://en.wikipedia.org/wiki/BSD_licenses#3-clause_license_.28.22New_BSD_License.22.29

"""
egversion = __doc__.split()[1]

__all__ = ['timerbox']

import sys, os
#import string
import traceback

#--------------------------------------------------
# check python version and take appropriate action
#--------------------------------------------------
"""
From the python documentation:

sys.hexversion contains the version number encoded as a single integer. This is
guaranteed to increase with each version, including proper support for non-
production releases. For example, to test that the Python interpreter is at
least version 1.5.2, use:

if sys.hexversion >= 0x010502F0:
    # use some advanced feature
    ...
else:
    # use an alternative implementation or warn the user
    ...
"""


if sys.hexversion >= 0x020600F0:
    runningPython26 = True
else:
    runningPython26 = False

if sys.hexversion >= 0x030000F0:
    runningPython3 = True
else:
    runningPython3 = False

try:
    from PIL import Image   as PILImage
    from PIL import ImageTk as PILImageTk
    PILisLoaded = True
except:
    PILisLoaded = False


if runningPython3:
    from tkinter import *
    import tkinter.filedialog as tk_FileDialog
    from io import StringIO
else:
    from Tkinter import *
    import tkFileDialog as tk_FileDialog
    from StringIO import StringIO

def write(*args):
    args = [str(arg) for arg in args]
    args = " ".join(args)
    sys.stdout.write(args)

def writeln(*args):
    write(*args)
    sys.stdout.write("\n")

say = writeln

def denyWindowManagerClose():
    """ don't allow WindowManager close
    """
    x = Tk()
    x.withdraw()
    x.bell()
    x.destroy()

rootWindowPosition = "+300+200"

PROPORTIONAL_FONT_FAMILY = ("MS", "Sans", "Serif")
MONOSPACE_FONT_FAMILY    = ("Courier")

PROPORTIONAL_FONT_SIZE  = 10
MONOSPACE_FONT_SIZE     =  9  #a little smaller, because it it more legible at a smaller size
TEXT_ENTRY_FONT_SIZE    = 12  # a little larger makes it easier to see

#STANDARD_SELECTION_EVENTS = ["Return", "Button-1"]
STANDARD_SELECTION_EVENTS = ["Return", "Button-1", "space"]

# Initialize some global variables that will be reset later
__choiceboxMultipleSelect = None
__widgetTexts = None
__replyButtonText = None
__choiceboxResults = None
__firstWidget = None
__enterboxText = None
__enterboxDefaultText=""
__multenterboxText = ""
choiceboxChoices = None
choiceboxWidget = None
entryWidget = None
boxRoot = None
ImageErrorMsg = (
    "\n\n---------------------------------------------\n"
    "Error: %s\n%s")
    
#-------------------------------------------------------------------
# utility routines
#-------------------------------------------------------------------
# These routines are used by several other functions in the EasyGui module.

def __buttonEvent(event):
    """
    Handle an event that is generated by a person clicking a button.
    """
    global  boxRoot, __widgetTexts, __replyButtonText
    __replyButtonText = __widgetTexts[event.widget]
    boxRoot.quit() # quit the main loop

#-------------------------------------------------------------------

def __put_buttons_in_buttonframe(choices):
    """Put the buttons in the buttons frame
    """
    global __widgetTexts, __firstWidget, buttonsFrame

    __firstWidget = None
    __widgetTexts = {}

    i = 0

    for buttonText in choices:
        tempButton = Button(buttonsFrame, takefocus=1, text=buttonText)
        bindArrows(tempButton)
        tempButton.pack(expand=YES, side=LEFT, padx='1m', pady='1m', ipadx='2m', ipady='1m')

        # remember the text associated with this widget
        __widgetTexts[tempButton] = buttonText

        # remember the first widget, so we can put the focus there
        if i == 0:
            __firstWidget = tempButton
            i = 1

        # for the commandButton, bind activation events to the activation event handler
        commandButton  = tempButton
        handler = __buttonEvent
        for selectionEvent in STANDARD_SELECTION_EVENTS:
            commandButton.bind("<%s>" % selectionEvent, handler)

def bindArrows(widget):
    widget.bind("<Down>", tabRight)
    widget.bind("<Up>"  , tabLeft)

    widget.bind("<Right>",tabRight)
    widget.bind("<Left>" , tabLeft)

def tabRight(event):
    boxRoot.event_generate("<Tab>")

def tabLeft(event):
    boxRoot.event_generate("<Shift-Tab>")
    
#-------------------------------------------------------------------
# timerbox
#-------------------------------------------------------------------

def timerbox(msg="",title=" "
    ,choices=None
    ,time=10
    , image=None
    , root=None
    
    ):
    """
    Display a msg, a title, and a set of buttons.
    The buttons are defined by the members of the choices list.
    Return the text of the button that the user selected.

    @arg msg: the msg to be displayed.
    @arg title: the window title
    @arg choices: a list or tuple of the choices to be displayed
    """
    global boxRoot, __replyButtonText, __widgetTexts, buttonsFrame


    # Initialize __replyButtonText to the first choice.
    # This is what will be used if the window is closed by the close button.
    if choices:
        __replyButtonText = choices[0]
    else:
        __replyButtonText = None
        
    if root:
        root.withdraw()
        boxRoot = Toplevel(master=root)
        boxRoot.withdraw()
    else:
        boxRoot = Tk()
        boxRoot.withdraw()

    boxRoot.protocol('WM_DELETE_WINDOW', denyWindowManagerClose )
    boxRoot.title(title)
    boxRoot.iconname('Dialog')
    boxRoot.geometry(rootWindowPosition)
    boxRoot.minsize(400, 100)

    # ------------- define the messageFrame ---------------------------------
    messageFrame = Frame(master=boxRoot)
    messageFrame.pack(side=TOP, fill=BOTH)

    # ------------- define the imageFrame ---------------------------------
    tk_Image = None
    if image:
        imageFilename = os.path.normpath(image)
        junk,ext = os.path.splitext(imageFilename)

        if os.path.exists(imageFilename):
            if ext.lower() in [".gif", ".pgm", ".ppm"]:
                tk_Image = PhotoImage(master=boxRoot, file=imageFilename)
            else:
                if PILisLoaded:
                    try:
                        pil_Image = PILImage.open(imageFilename)
                        tk_Image = PILImageTk.PhotoImage(pil_Image, master=boxRoot)
                    except:
                        msg += ImageErrorMsg % (imageFilename,
                            "\nThe Python Imaging Library (PIL) could not convert this file to a displayable image."
                            "\n\nPIL reports:\n" + exception_format())

                else:  # PIL is not loaded
                    msg += ImageErrorMsg % (imageFilename,
                    "\nI could not import the Python Imaging Library (PIL) to display the image.\n\n"
                    "You may need to install PIL\n"
                    "(http://www.pythonware.com/products/pil/)\n"
                    "to display " + ext + " image files.")

        else:
            msg += ImageErrorMsg % (imageFilename, "\nImage file not found.")

    if tk_Image:
        imageFrame = Frame(master=boxRoot)
        imageFrame.pack(side=TOP, fill=BOTH)
        label = Label(imageFrame,image=tk_Image)
        label.image = tk_Image # keep a reference!
        label.pack(side=TOP, expand=YES, fill=X, padx='1m', pady='1m')

    # ------------- define the buttonsFrame ---------------------------------
    if choices:
        buttonsFrame = Frame(master=boxRoot)
        buttonsFrame.pack(side=TOP, fill=BOTH)

    # -------------------- place the widgets in the frames -----------------------
    messageWidget = Message(messageFrame, text=msg, width=400)
    messageWidget.configure(font=(PROPORTIONAL_FONT_FAMILY,PROPORTIONAL_FONT_SIZE))
    messageWidget.pack(side=TOP, expand=YES, fill=X, padx='3m', pady='3m')

    counterWidget = Message(messageFrame, text=str(time), width=400)
    counterWidget.configure(font=(PROPORTIONAL_FONT_FAMILY,PROPORTIONAL_FONT_SIZE))
    counterWidget.pack(side=TOP, expand=YES, fill=X, padx='3m', pady='3m')

    if choices:
        __put_buttons_in_buttonframe(choices)

    # -------------- the action begins -----------
    # put the focus on the first button
    if choices:
        __firstWidget.focus_force()

    global __after
    
    def countdown(seconds):
        global __after
        if seconds > 0:
            seconds -= 1
            counterWidget.config(text=str(seconds))
            __after = boxRoot.after(1000, lambda x=seconds: countdown(x))
            #print( "DEBUG: __after B:", __after )
        else:
            boxRoot.quit()
        
    __after = boxRoot.after(1000, lambda x=time: countdown(x))
    #print( "DEBUG: __after A:", __after )

    boxRoot.deiconify()
    boxRoot.mainloop()
    #print( "DEBUG: after_cancel:", __after )
    boxRoot.after_cancel(__after)
    boxRoot.destroy()
    if root: root.deiconify()
    return __replyButtonText


#-----------------------------------------------------------------------------------------

if __name__ == '__main__':
    timerbox('Time to the end of the World', 'Countdown', time=5)

    result = timerbox('Last change to save the World', 'Countdown', choices=['BUM!', 'Save the World'], time=5)

    if result == 'BUM!':
        timerbox('Time to BUM !!!', 'Countdown', choices=['OK'], time=5)
    else:
        timerbox('You saved the World !', 'Countdown', choices=['OK'], time=5)
