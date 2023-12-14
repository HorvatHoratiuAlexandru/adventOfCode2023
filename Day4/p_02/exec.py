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

ticket_count = dict()

def count_tickets(id, w, n):
    wins = len([w_i for w_i in w if w_i in n])
    id_cpy = id
    count = 1

    if wins == 0:
        ticket_count[id]=count
        return count


    for cpy in range(1, wins+1):
        id_cpy += 1
        count += count_tickets(id_cpy, input[id_cpy]["w"], input[id_cpy]["n"])

    ticket_count[id] = count
    return count

for key in input:
    if not ticket_count.get(key):
        count_tickets(key, input[key]["w"], input[key]["n"])

print(sum([v for v in ticket_count.values()]))