from typing import List
import functools

inputs: List[str] = []

with open("input.txt", "r+") as f:
    for line in f:
        inputs.append(line)

COLORS = [
    "r",
    "g",
    "b"
]

DIGITS = ['0','1','2','3','4','5','6','7','8','9']

answer_list = []
for input in inputs:
    line = input.replace(" ", "")
    _ , rounds = line.split(":")[0][4:], line.split(":")[1].split(";")
    min_set = dict()
    for round in rounds:  
        for c in range(len(round)):
            if round[c] in COLORS and round[c -1] in DIGITS:
                i = 1
                while(round[c - i] in DIGITS):
                    i += 1
                i = i - 1
                if round[c] in min_set.keys():
                    if int(round[c-i:c]) > min_set[round[c]]:
                        min_set[round[c]] = int(round[c-i:c])
                else:
                    min_set[round[c]] = int(round[c-i:c])
    
    answer_list.append(functools.reduce(lambda a, b: a*b, min_set.values()))

print(sum(answer_list))