def calculate_safety_factor(input_data, time=100, width=101, height=103):
    from collections import defaultdict

    # Parse input data
    robots = []
    for line in input_data.strip().split("\n"):
        pos, vel = line.split(" ")
        px, py = map(int, pos[2:].split(","))
        vx, vy = map(int, vel[2:].split(","))
        robots.append(((px, py), (vx, vy)))

    # Calculate final positions after `time` seconds
    final_positions = []
    for (px, py), (vx, vy) in robots:
        final_x = (px + vx * time) % width
        final_y = (py + vy * time) % height
        final_positions.append((final_x, final_y))

    # Determine quadrants
    mid_x, mid_y = width // 2, height // 2
    quadrant_counts = defaultdict(int)
    
    for x, y in final_positions:
        if x == mid_x or y == mid_y:
            continue  # Skip middle robots
        elif x < mid_x and y < mid_y:
            quadrant_counts["Q1"] += 1
        elif x >= mid_x and y < mid_y:
            quadrant_counts["Q2"] += 1
        elif x < mid_x and y >= mid_y:
            quadrant_counts["Q3"] += 1
        elif x >= mid_x and y >= mid_y:
            quadrant_counts["Q4"] += 1

    # Calculate safety factor
    q1, q2, q3, q4 = (quadrant_counts["Q1"], quadrant_counts["Q2"], 
                       quadrant_counts["Q3"], quadrant_counts["Q4"])
    safety_factor = q1 * q2 * q3 * q4

    return safety_factor

def find_christmas_tree(input_data, width=101, height=103, max_time=20000):
    from collections import defaultdict

    # Parse input data
    robots = []
    for line in input_data.strip().split("\n"):
        pos, vel = line.split(" ")
        px, py = map(int, pos[2:].split(","))
        vx, vy = map(int, vel[2:].split(","))
        robots.append(((px, py), (vx, vy)))

    # Simulate positions and look for the smallest bounding box
    min_area = float('inf')
    best_time = 0
    best_positions = []

    for t in range(max_time):
        positions = []
        for (px, py), (vx, vy) in robots:
            final_x = (px + vx * t) % width
            final_y = (py + vy * t) % height
            positions.append((final_x, final_y))
        
        # Find bounding box
        xs, ys = zip(*positions)
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        area = (max_x - min_x + 1) * (max_y - min_y + 1)

        # If the bounding box is the smallest, update
        if area < min_area:
            min_area = area
            best_time = t
            best_positions = positions

    return best_time, best_positions

# Load data from the provided file
file_path = '/Users/jonathanborer/Desktop/Programmieren WI/advent/advent_data/day14.txt'
with open(file_path, 'r') as f:
    input_data = f.read().strip()

# Calculate safety factor for part 1
safety_factor = calculate_safety_factor(input_data, time=100, width=101, height=103)
print("Safety Factor (Part 1):", safety_factor)

# Find time when robots align into a Christmas tree for part 2
alignment_time, alignment_positions = find_christmas_tree(input_data, width=101, height=103, max_time=20000)
print("Alignment Time (Part 2):", alignment_time)
