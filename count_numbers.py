import os
dosya1 = open("file_10000integers_A.txt", "r")
home = os.getcwd()
path2 = home + "/file_10000integers_A.txt"

a = 0

lst3 = []
with open(path2, "r") as file:
    lines = file.readlines()
    for line in lines:
        as_string = line
        string_list = as_string.split(", ")
        for s in string_list:
            lst3.append(int(s))
            a += 1
def count_different(lst3):
    sett = set(lst3)
    s = len(sett)
    print(s)


def count_occurrences(lst3):
    dct = {}
    tup = tuple(lst3)
    for i in tup:
        if i not in dct:
            b = tup.count(i)
            dct[i] = b
            
    print(dct)
    value_sorted = sorted(dct.values())
    n = len(value_sorted)
    print(dct.items, value_sorted[n-5:n]) 

count_occurrences(lst3)