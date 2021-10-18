import os

home = os.getcwd()
path = home + "/holy_grail.txt"

def read_file(file_path):
    with open(path, "r", encoding='utf-8') as file:
        for rows in file:
            print(f"\nRead", len(rows), "lines from file", path)


def get_words(row):
    words = []
    with open(path, "r", encoding='utf-8') as file:
        for rows in file:
            splitWords = rows.split()
            words.append(splitWords)
            
