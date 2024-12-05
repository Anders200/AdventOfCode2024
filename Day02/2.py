def is_safe(levels):
    increasing = all(levels[i] < levels[i + 1] and 1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] and 1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing

def can_be_safe_with_one_removal(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True
    return False

with open("2.txt", "r") as file:
    liststr = file.read().strip().split("\n")

safeLevels = 0

for line in liststr:
    levels = line.split(" ")
    levels = [int(i) for i in levels]
    if is_safe(levels):
        safeLevels += 1

print(safeLevels) # task 1

safeLevelsAfterOneOrLessRemovals = 0

for line in liststr:
    levels = line.split(" ")
    levels = [int(i) for i in levels]

    if can_be_safe_with_one_removal(levels):
        safeLevelsAfterOneOrLessRemovals += 1

print(safeLevelsAfterOneOrLessRemovals) # task 2