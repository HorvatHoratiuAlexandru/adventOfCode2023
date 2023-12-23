import math
moves = []
tree = dict()
heads = []
targets = []

with open("input.txt", "r+") as f:
    parsing_moves = True
    for line in f:
        if line == "\n":
            parsing_moves = False
            continue

        if parsing_moves:
            for move in line.strip():
                moves.append(move)
        else:
            line_holder = line.strip().replace(" ", "").split("=")
            id = line_holder[0]
            leafs = line_holder[1]
            
            left = leafs.split(",")[0].replace("(", "")
            right = leafs.split(",")[1].replace(")", "")

            if id[2] == "A":
                heads.append(id)

            if id[2] == "Z":
                targets.append(id)

            tree[id] = {"L": left, "R": right}

m_i = 0            
f = dict()
f[0] = dict()

for key in tree:
    f[0][key] = key

while m_i < len(moves):
    f[m_i+1] = dict()

    for key in tree:
        f[m_i+1][key] = tree.get(f.get(m_i)[key])[moves[m_i]]
    
    m_i +=1


def sol(head, n):

    m_i = 1
    no_moves = 0

    while m_i < len(moves) +1:
        no_moves += 1
        if f[m_i][head] in targets:      
            if no_moves > n:
                break
            
        m_i+=1

        if m_i > len(moves):
            head = f[m_i - 1][head]
            m_i = 1
    
    return no_moves

max_moves = [0 for _ in heads]

while min(max_moves) == 0:
    h = 0

    while h<len(heads):
        if max_moves[h] == min(max_moves):
            max_moves[h] = sol(heads[h], max_moves[h])
            break
        h += 1

print(math.lcm(*max_moves))
