from typing import List
inputs: List[str] = []

with open("input.txt", "r+") as f:
    for line in f:
        inputs.append(line)

COLORS = {
    "r": 12,
    "g": 13,
    "b": 14
}

DIGITS = ['0','1','2','3','4','5','6','7','8','9']

answer_list = []
for input in inputs:
    line = input.replace(" ", "")
    game, rounds = line.split(":")[0][4:], line.split(":")[1].split(";")

    is_valid = True
    for round in rounds:
        for c in range(len(round)):
            if round[c] in COLORS.keys() and round[c -1] in DIGITS:
                i = 1
                while(round[c - i] in DIGITS):
                    i += 1
                i = i - 1
                if int(round[c-i:c]) > COLORS[round[c]]:
                    is_valid = False
    
    if is_valid:
        answer_list.append(int(game))

print(sum(answer_list))