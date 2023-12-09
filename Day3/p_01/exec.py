input = []
with open("input.txt", "r+") as f:
    for line in f:
        input.append(list(line.strip()))

DIGITS = ["0", "1", "2","3","4","5","6","7","8","9"]
result_list = []

def nums(i,j):
    num = None

    if i < 0 or j < 0:
        return num
    
    if i>=len(input) or j>=len(input[i]):
        return num
    
    if input[i][j] == ".":
        return num
    
    if input[i][j] in DIGITS:
        num = input[i][j]
        input[i][j] = "."
        left = nums(i, j-1)
        right = nums(i, j+1)

        if left:
            num = left + num
        if right:
            num = num + right


    return num


for row in range(len(input)):
    for column in range(len(input[row])):
        if input[row][column] not in DIGITS and input[row][column] != ".":
            surrounding_nums = []

            surrounding_nums.append(nums(row, column-1))
            surrounding_nums.append(nums(row, column+1))
            surrounding_nums.append(nums(row-1, column))
            surrounding_nums.append(nums(row+1, column))
            surrounding_nums.append(nums(row-1, column-1))
            surrounding_nums.append(nums(row+1, column-1))
            surrounding_nums.append(nums(row+1, column+1))
            surrounding_nums.append(nums(row-1, column+1))

            for n in surrounding_nums:
                if n:
                    result_list.append(int(n))

print(sum(result_list))
