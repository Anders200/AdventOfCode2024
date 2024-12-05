with open("4.txt", "r") as file:
    content = file.read().strip().split("\n")

n = len(content)
m = len(content[0])

def findAllXmas(x, y): # start on X and traverse in every direction
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),  # right, left, down, up
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # down-right, down-left, up-right, up-left
    ]
    word = "XMAS"
    occurrences = 0
    for dx, dy in directions:
        if not (0 <= x + dx * (len(word) - 1) < n and 0 <= y + dy * (len(word) - 1) < m):
            continue

        if all(content[x + dx * i][y + dy * i] == word[i] for i in range(len(word))):
            occurrences += 1
    return occurrences

occurrences = 0

for i in range(n):
    for j in range(m):
        if content[i][j] == "X":
            occurrences += findAllXmas(i, j)

print(occurrences) # task 1

def is_valid_mas_or_sam(x, y, dx, dy):
    words = ["MAS", "SAM"]
    for word in words:
        valid = True
        for i in range(len(word)):
            nx, ny = x + dx * i, y + dy * i
            if nx < 0 or ny < 0 or nx >= n or ny >= m or content[nx][ny] != word[i]:
                valid = False
                break
        if valid:
            return True
    return False

def count_x_mas():
    occurrences = 0
    for i in range(1, n - 1):  # Center of the X
        for j in range(1, m - 1):
            # Check both diagonals
            if (
                is_valid_mas_or_sam(i - 1, j - 1, 1, 1) and  # Top-left MAS/SAM
                is_valid_mas_or_sam(i - 1, j + 1, 1, -1)    # Top-right MAS/SAM
            ):
                occurrences += 1
    return occurrences

print(count_x_mas()) # task 2