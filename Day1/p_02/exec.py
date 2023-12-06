from typing import List

STR_DIGITS = {'zero':'0',
              'one':'1',
              'two':'2',
              'three':'3',
              'four':'4', 
              'five':'5', 
              'six':'6', 
              'seven':'7', 
              'eight':'8', 
              'nine':'9'}



input_list: List[str] = []

with open("input.txt", "r+") as input_file:
    for input in input_file:
        input_list.append(input)


result_list: List[str] = []


for input in input_list:
    num_index = dict()
    for c_i in range(len(input)):
        if input[c_i] in STR_DIGITS.values():
            num_index[c_i] = input[c_i]

        for str_num in STR_DIGITS.keys():
            if c_i + len(str_num) < len(input):
                if input[c_i:c_i+len(str_num)] == str_num:
                    num_index[c_i] = str_num
    left = num_index.get(min(num_index.keys()))
    right = num_index.get(max(num_index.keys()))

    if left in STR_DIGITS.keys():
        left = STR_DIGITS.get(left)

    if right in STR_DIGITS.keys():
        right = STR_DIGITS.get(right)


    result_list.append(int(left+right))

print(sum(result_list))