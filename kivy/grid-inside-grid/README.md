
# Examples

- 1. GridLayout as main widget.
- 2. Widget as main widget and Gridlayout inside Widget.
- 3. Gridlayout as main widget and second Gridlayout inside first Gridlayout.

## 1. GridLayout as main widget. 

- it uses all window 
- it resizes when window change size
- it can't change `width`, `height` and `position`

At start: 

![#1](images/example1-normal.png?raw=true)

## 2. Widget as main widget and Gridlayout inside Widget.

- it doesn't use all window
- it doesn't resize when window change size
- it **can** change `width`, `height` and `position`

At start: 

![#1](images/example2-normal.png?raw=true)

After changing window's size:

![#1](images/example2-resized.png?raw=true)

## 3. Gridlayout as main widget and second Gridlayout inside first Gridlayout.

- it use all window
- it resize when window change size
- it **can** change `width`, `height` and `position`

At start: 

![#1](images/example3-normal.png?raw=true)

After changing window's size:

![#1](images/example3-resized.png?raw=true)
