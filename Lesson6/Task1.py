
def func1(list):
    string = ""
    for item in list:
        string = string + chr(item)
    return string


def func2(list):
    return reduce(lambda string, item: string + chr(item), list, "")


def func3(list):
    string = ""
    for character in map(chr, list):
        string = string + character
    return string


def func4(list):
    string = ""
    lchr = chr
    for item in list:
        string = string + lchr(item)
    return string


def func5(list):
    string = ""
    for i in range(0, 256, 16): # 0, 16, 32, 48, 64, ...
        s = ""
        for character in map(chr, list[i:i+16]):
            s = s + character
        string = string + s
    return string


import string
def func6(list):
    return string.joinfields(map(chr, list), "")


import array
def func7(list):
     return array.array('b', list).tostring()