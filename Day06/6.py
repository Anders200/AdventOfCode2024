def find_initial_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in "^>v<":
                return (i, j, grid[i][j])

def count_guard_positions(grid):
    m = len(grid)
    n = len(grid[0])

    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    turn_order = {"^": ">", ">": "v", "v": "<", "<": "^"}
    
    guard_pos = [0, 0]
    guard_pos[0], guard_pos[1], guard_dir = find_initial_position(grid)
    
    visited = set()
    visited.add((guard_pos[0], guard_pos[1]))
    
    while True:
        # Calculate the next position
        di, dj = directions[guard_dir]
        next_pos = (guard_pos[0] + di, guard_pos[1] + dj)
        
        # Check if the next position is outside the map
        if not (0 <= next_pos[0] < m and 0 <= next_pos[1] < n):
            break
        
        # Check if there's an obstacle
        if grid[next_pos[0]][next_pos[1]] == "#":
            # Turn right
            guard_dir = turn_order[guard_dir]
        else:
            # Move forward
            guard_pos = next_pos
            visited.add(guard_pos)
    
    return len(visited)

def simulate_guard(grid, start_pos, start_dir, add_obstruction=None):
    m, n = len(grid), len(grid[0])
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    right_turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    visited_states = set()
    
    guard_pos = start_pos
    guard_dir = start_dir
    
    if add_obstruction:
        grid[add_obstruction[0]][add_obstruction[1]] = '#'
    
    while True:
        state = (guard_pos, guard_dir)
        if state in visited_states:
            # Loop detected
            if add_obstruction:
                grid[add_obstruction[0]][add_obstruction[1]] = '.'
            return True
        visited_states.add(state)
        
        i, j = guard_pos
        di, dj = directions[guard_dir]
        next_pos = (i + di, j + dj)
        
        # Check for boundaries
        if not (0 <= next_pos[0] < m and 0 <= next_pos[1] < n):
            if add_obstruction:
                grid[add_obstruction[0]][add_obstruction[1]] = '.'
            return False
        
        # Check for obstacles
        if grid[next_pos[0]][next_pos[1]] == '#':
            guard_dir = right_turn[guard_dir]
        else:
            guard_pos = next_pos

def count_obstruction_positions(grid):
    m, n = len(grid), len(grid[0])
    start_pos, start_dir = find_initial_position(grid)[:2], find_initial_position(grid)[2]

    valid_positions = set()
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.' and (i, j) != start_pos:
                if simulate_guard(grid, start_pos, start_dir, add_obstruction=(i, j)):
                    valid_positions.add((i, j))
        print(f"Progress: {i / m * 100:.2f}%\r", end="")
    return len(valid_positions)

# Read the input file
with open("6.txt", "r") as file:
    content = file.read().strip().split("\n")
    content = [list(line) for line in content]

print(count_guard_positions(content))  # Task 1
print(count_obstruction_positions(content))  # Task 2
