
Full working code is in files.


# askopenfile

- It gives file object. 

- To get file name you have to use `.name`

- To get data from file you don't need `open()` 

```python
file_object = filedialog.askopenfile(title="Select file")

print('file_object:', file_object)
print('file_object.name:', file_object.name)

data = file_object.read()
print(data)
```

# askopenfilename

- It gives file name. 

- To get data from file you need `open()` 

```python
filename = filedialog.askopenfilename(title="Select file")

print('filename:', filename)

data = open(filename).read()
print(data)
```
