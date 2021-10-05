
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.09.28
#
# title: parsing values inside () in psutil.sensors_temperatures() in Python in Ubuntu 20.04
# url: https://stackoverflow.com/questions/69362172/parsing-values-inside-in-psutil-sensors-temperatures-in-python-in-ubuntu-20/69364806?noredirect=1#comment122603404_69364806

# [parsing values inside () in psutil.sensors_temperatures() in Python in Ubuntu 20.04](https://stackoverflow.com/questions/69362172/parsing-values-inside-in-psutil-sensors-temperatures-in-python-in-ubuntu-20/69364806?noredirect=1#comment122603404_69364806)


import psutil

data = psutil.sensors_temperatures()
print('\n--- type ---')
print(type(data))  # dict
print('--- value ---')
print(data)

core = data['coretemp']
print('\n--- type ---')
print(type(core))  # list
print('--- value ---')
print(core)

item = core[0]
print('\n--- type ---')
print(type(item))  # object shwtemp
print('--- value ---')
print(item)
print('--- fields ---')
print('label   :', item.label)
print('current :', item.current)
print('high    :', item.high)
print('critical:', item.critical)

# -------------------------------------------------

data = psutil.sensors_temperatures()

print('\n--- First ---')
print('First:', data['coretemp'][0].current)

print('\n--- for-loop ---')
for item in data['coretemp']:
    print(item.label, ':', item.current)

