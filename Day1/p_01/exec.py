from typing import List

input_list: List[str] = []

with open("input.txt", "r+") as input_file:
    for input in input_file:
        input_list.append(input)

DIGITS = ["0", "1", "2","3","4","5","6","7","8","9"]
result: List[int] = []

for i in input_list:
    first_num: str = None
    second_num: str = None
    for c in range(len(i)):
        first_num = i[c] if i[c] in DIGITS and first_num is None else first_num
        second_num = i[len(i)- c -1] if i[len(i)- c -1] in DIGITS and second_num is None else second_num
    result.append(int(first_num+second_num))

print(sum(result))