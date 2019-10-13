def to_string(my_list, sep=', '):

    string = ''

    for char in my_list:
        if string:
            string = string + sep
        string = string + char

    return string

my_list = ['H','E','L','p']
print(to_string(my_list, '-'))
print(to_string(['a'], '-'))
print(to_string([], '-'))

def to_string(my_list, sep=', '):

    if not my_list:
        return ''

    string = my_list[0]

    for char in my_list[1:]:
        string = string + sep + char

    return string

my_list = ['H','E','L','p']
print(to_string(my_list, '-'))
print(to_string(['a'], '-'))
print(to_string([], '-'))
