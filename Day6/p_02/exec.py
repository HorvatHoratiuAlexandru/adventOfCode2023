time = 0
distance = 0

with open("input.txt", "r+") as f:
    time_line = f.readline().strip().replace(" ", "")
    distance_line = f.readline().strip().replace(" ", "")
   
    time = int(time_line.split(":")[1])
    distance =  int(distance_line.split(":")[1])

ways_to_beat = 0
for t in range(0, time):
    if t * (time - t) > distance:
        ways_to_beat +=1

print(ways_to_beat) 