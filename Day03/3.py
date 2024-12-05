import re

with open("3.txt", "r") as file:
    content = file.read().strip()

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

mul_matches = re.findall(mul_pattern, content)
mul_matches_indexes = [m.start() for m in re.finditer(mul_pattern, content)]

sumMuls = 0
for mul in mul_matches:
    a, b = map(int, mul)
    sumMuls += a * b

print(sumMuls) # task 1

do_matches = [m.start() for m in re.finditer(do_pattern, content)]
dont_matches = [m.start() for m in re.finditer(dont_pattern, content)]

sumMulsWithDos = 0
do_enabled = True
j, k = 0, 0

for i in range(len(mul_matches_indexes)):
    index = mul_matches_indexes[i]
    
    while j < len(do_matches) and index > do_matches[j]:
        do_enabled = True
        j += 1
    
    while k < len(dont_matches) and index > dont_matches[k]:
        do_enabled = False
        k += 1

    if do_enabled:
        a, b = map(int, mul_matches[i])
        sumMulsWithDos += a * b

print(sumMulsWithDos) # task 2