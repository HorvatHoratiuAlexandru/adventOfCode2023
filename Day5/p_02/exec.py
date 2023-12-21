from typing import List

MAPS = ["seeds", "seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
input = dict()

for map in MAPS:
    input[map] = []

whitespace_counter = 0
with open("input.txt", "r+") as f:
    
    for line in f:
        if line == "\n":
            whitespace_counter +=1
        else:
            if MAPS[0] in line:
                holder = line.replace("\n", "").split(" ")
                for n in range(1, len(holder)):
                    input[MAPS[0]].append(holder[n])
            if whitespace_counter == 0 and MAPS[0] not in line:
                holder = line.replace("\n", "").split(" ")
                for n in range(0, len(holder)):
                    input[MAPS[0]].append(holder[n])

            if whitespace_counter > 0 and whitespace_counter < len(MAPS):
                if MAPS[whitespace_counter] in line:
                    pass
                else:
                    holder = line.replace("\n", "").split(" ")
                    input[MAPS[whitespace_counter]].append(holder)

                    
seeds = [int(s_i) for index, s_i in enumerate(input["seeds"]) if index % 2 == 0]
ranges = [int(s_i) for index, s_i in enumerate(input["seeds"]) if index % 2 != 0]

answer_list = []

def get_min_seeds(seed, rg, map):
    sd = seed
    for counter in range(map, len(MAPS)):
        for map_line in input[MAPS[counter]]:
            src = int(map_line[1])
            rng = int(map_line[2])
            dst = int(map_line[0])

            if sd >= src and sd <= src + rng - 1:

                if sd + rg -1 > src + rng -1:
                    new_range = (sd+rg) - (src+rng)
                    new_seed = src+rng
                    rg = new_seed-sd
                    get_min_seeds(new_seed, new_range, counter)

                sd = sd + (dst - src)
                break

    answer_list.append(sd)

for s, r in zip(seeds, ranges):
    get_min_seeds(s,r,1)

# Dunno why the answer is offset by + 1 ????
print(min(answer_list))