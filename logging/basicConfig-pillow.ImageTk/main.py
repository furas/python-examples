import tkinter as tk # Python 3.x
from PIL import ImageTk, Image
import logging

def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) # root level

    # console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG) # level for console
    logger.addHandler(ch)
    
    # file
    fh = logging.FileHandler('mylog-2.log')
    fh.setLevel(logging.DEBUG) # level for file
    logger.addHandler(fh)
    
    return logger

if __name__ == "__main__":

    # ImageTk already created logger so basicConfig can't change level 
    # and you can see messages from  ImageTk in logger
    
    logging.basicConfig(filename='mylog-1.log', filemode='a', format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    logging.info('Test #1')

    # create own logger to save only own messages
    logger = create_logger()
    logger.info('Test #2')
    
    root = tk.Tk()

    # png create messages in log
    ImageTk.PhotoImage(Image.open('Obrazy/images/ball.png'))
    
    root.mainloop()
