# Given:
time_points = [0, 1, 2, 3, 4]  # seconds
particles = {"P1", "P2", "P3"}  # unique IDs
trajectories = {
    "P1": [(1.0, 2.0), (0.5, 0.3), (0.1, -0.1), (0.0, 0.01), (-0.2, -0.3)],
    "P2": [(2.0, 1.0), (1.8, 0.9), (1.5, 0.6), (1.0, 0.2), (0.5, -0.1)],
    "P3": [(-1.0, -1.0), (-0.5, -0.5), (0.0, 0.0), (0.2, 0.1), (0.3, 0.4)]
}

# Task: Find which particles came within 0.2 units of (0,0)

def norm_check(coords) -> bool:
     if (coords[0]**2 + coords[1]**2) <= 0.2:
         return True
     else:
         return False

for p in particles:
    for ii in range(len(trajectories[p])):
        if norm_check(trajectories[p][ii]):
            print(p)
            break
