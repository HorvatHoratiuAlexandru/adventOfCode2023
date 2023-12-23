moves = []
tree = dict()
head = "AAA"

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


            tree[id] = {"L": left, "R": right}

#--- SOLUTION 1
m_i = 0
no_moves = 0

while m_i < len(moves):
    
    no_moves += 1
    head = tree.get(head)[moves[m_i]]
    if head == "ZZZ":
        break
    
    m_i += 1

    if m_i == len(moves):
        m_i = 0

print(no_moves)


#--- SOLUTION 2

# m_i = 0            
# f = dict()
# f[0] = dict()

# for key in tree:
#     f[0][key] = key

# while m_i < len(moves):
#     f[m_i+1] = dict()

#     for key in tree:
#         f[m_i+1][key] = tree.get(f.get(m_i)[key])[moves[m_i]]
    
#     m_i +=1

# target = "ZZZ"
# m_i = 1
# no_moves = 0

# while m_i < len(moves) +1:
#     if f[m_i][head] == target:
#         no_moves += m_i
#         break
    
#     m_i+=1

#     if m_i > len(moves):
#         no_moves += m_i - 1
#         head = f[m_i - 1][head]
#         m_i = 1


# print(no_moves)
