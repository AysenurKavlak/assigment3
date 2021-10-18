dosya = open("file_10000integers_B.txt", "r")
import os
import math
home = os.getcwd()
path = home + "/file_10000integers_B.txt"

a = 0

lst = []
with open(path, "r") as file:
    as_string = file.read()
    string_list = as_string.split(":")
    for s in string_list:
        lst.append(int(s))

mean = sum(lst) / len(lst)


for i in lst:
    a = (i - mean)**2
    lst2 = []
    lst2.append(a)


variance = sum(lst2) / (len(lst) - 1)


print("B standart deviation", math.sqrt(variance))

dosya.close()

dosya1 = open("file_10000integers_A.txt", "r")
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


mean2 = sum(lst3) / len(lst3)


for i in lst3:
    a = (i - mean2)**2
    lst4 = []
    lst4.append(a)


variance2 = sum(lst4) / (len(lst3) - 1)


print("A standart deviation", math.sqrt(variance))



