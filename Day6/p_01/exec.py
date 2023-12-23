times = []
distances = []

with open("input.txt", "r+") as f:
    time_line = f.readline().strip()
    distance_line = f.readline().strip()
    
    times = [int(t_i) for t_i in time_line.split(":")[1].split(" ") if t_i != ""]
    distances = [int(d_i) for d_i in distance_line.split(":")[1].split(" ") if d_i != ""]

result = []

for t,d in zip(times, distances):
    ways_to_beat=0
    for time in range(0, t):
        if time * (t-time) > d:
            ways_to_beat +=1
    
    if ways_to_beat > 0:
        result.append(ways_to_beat)

r=1

for w in result:
   r = r*w

print(r) 