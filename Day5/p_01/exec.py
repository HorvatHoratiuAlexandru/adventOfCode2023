from typing import List

MAPS = ["seeds", "seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
input = dict()

for map in MAPS:
    input[map] = []

whitespace_counter = 0
with open("test.txt", "r+") as f:
    
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


location_list = []

for seed in input["seeds"]:
    sd = int(seed)
    
    for counter in range(1, len(MAPS)):
        for map_line in input[MAPS[counter]]:
            src = int(map_line[1])
            rng = int(map_line[2])
            dst = int(map_line[0])
        
            if sd >= src and sd <= src + rng:
                sd = sd + (dst - src)
                break
    location_list.append(sd)

print(min(location_list))

    

        
    






