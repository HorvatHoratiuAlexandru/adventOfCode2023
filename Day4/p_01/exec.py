from typing import List

input = dict()
count = 0
with open("input.txt", "r+") as f:
    for line in f:
        count += 1
        splited_line = line.split(":")
        left, right = splited_line[0], splited_line[1]
        winning_nums = right.split("|")[0].strip()
        my_nums = right.split("|")[1].strip()
        
        input[count] = {
            "w":[int(n) for n in winning_nums.split(" ") if n != ""],
            "n":[int(n) for n in my_nums.split(" ") if n != ""]
        }


total_score = 0
for game in input.values():
    game_score = -1
    nums: List = game["w"] + game["n"]
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            game_score += 1
    if game_score > -1:    
        total_score = total_score + pow(2, game_score)

print(total_score)