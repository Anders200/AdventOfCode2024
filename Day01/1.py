with open("1.txt", "r") as file:
    liststr = file.read().strip().split("\n")

list1 = []
list2 = []

for line in liststr:
    parts = line.split()
    if len(parts) >= 2:
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

list1.sort()
list2.sort()

listsum = 0
for i in range(len(list1)):
    listsum += abs(list1[i] - list2[i])

print(listsum) # task 1

count_dict = {}
for number in list2:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

similarityScore = 0
for number in list1:
    if number in count_dict:
        similarityScore += number * count_dict[number]

print(similarityScore) # task 2