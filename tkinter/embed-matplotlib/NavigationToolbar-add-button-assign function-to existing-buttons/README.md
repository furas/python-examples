It is example from Matplotlib documentation: [Embedding In Tk](https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_sgskip.html)

Changes:

- adding own button to `NavigationToolbar2Tk`

`NavigationToolbar2Tk` is assigned to variable `toolbar` so `Button` needs it as first argument (parent widget)

```python
Button(toolbar,...)
```
   
- assigning function to existing buttons in `NavigationToolbar2Tk`

To display all items in `NavigationToolbar2Tk` (not only buttons)

```python
for item in toolbar.children: 
    print(item) 
    #print(item.config())
```

So we can see names/ids of buttons and we can use them to assign function

```python
def my_function():
    print("Left Arrow")

# add function to button with left arrow
toolbar.children['!button2'].config(command=my_function)
````
