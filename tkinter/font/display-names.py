#!/usr/bin/env python3

import tkinter as tk

from tkinter.font import families
root = tk.Tk()

families = tk.font.families()
print('\nnumber:', len(families))
print('\n'.join(sorted(families)))

names = tk.font.names()
print('\nnumber:', len(names))
print('\n'.join(sorted(names)))

