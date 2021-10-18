import os
def print_subdirectory(path):
    lst = os.scandir(path)
    print(lst)
    for i in lst:
        if i.is_file():
            print("FILE", i)
        else: 
            print("Folder", i)
            lst2 = os.scandir(i)
            for j in lst2:
                if i.is_file():
                    print(" ", "FILE", j)
                else: 
                    print(" ", "Folder", j)


path = os.getcwd()
print_subdirectory(path)
