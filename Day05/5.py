def parse_input(input_data):
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = []
    for line in rules_section.splitlines():
        x, y = map(int, line.split("|"))
        rules.append((x, y))
    updates = [
        list(map(int, update.split(",")))
        for update in updates_section.splitlines()
    ]
    return rules, updates


def is_valid_update(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def find_middle_page(update):
    n = len(update)
    return update[n // 2]


def sum_middle_pages(rules, updates):
    valid_updates = [
        update for update in updates if is_valid_update(update, rules)
    ]
    middle_pages = [find_middle_page(update) for update in valid_updates]
    return sum(middle_pages)

from collections import defaultdict, deque

def topological_sort(nodes, edges):
    # Build graph
    graph = defaultdict(list)
    in_degree = {node: 0 for node in nodes}
    for x, y in edges:
        if x in nodes and y in nodes:  # Only include relevant rules
            graph[x].append(y)
            in_degree[y] += 1

    # Kahns algorithm
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_list = []

    while queue:
        current = queue.popleft()
        sorted_list.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_list

def reorder_update(update, rules):
    return topological_sort(update, rules)

def sum_corrected_middle_pages(rules, updates):
    valid_updates = []
    invalid_updates = []

    for update in updates:
        if is_valid_update(update, rules):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    # Correct the invalid updates
    corrected_updates = [reorder_update(update, rules) for update in invalid_updates]

    # Find the middle page of each corrected update
    middle_pages = [find_middle_page(update) for update in corrected_updates]

    return sum(middle_pages)

with open("5.txt", "r") as file:
    input_data = file.read()

rules, updates = parse_input(input_data)
print(sum_middle_pages(rules, updates))
print(sum_corrected_middle_pages(rules, updates))
