#Rosalind set6 task1
import json

text = []
with open("task1.txt") as f:
    for line in f:
        text.append(line.strip())
f.close()


_end = 'end'
def trie_construction(input_array):
    root = dict()
    for i in range(len(input_array)):
        current_dict = root
        for j in range(len(input_array[i])):
            current_symbol = input_array[i][j]
            current_dict = current_dict.setdefault(current_symbol, {})
        current_dict[_end] = _end
    return root

def my_print(input_dict):
    for k, v in input_dict.items():
        if isinstance(v, dict):
            my_print(v)

print(my_print(trie_construction(text)))

