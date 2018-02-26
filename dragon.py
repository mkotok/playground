import numpy as np
import matplotlib.pyplot as plt


# form turning directions
iterations = 12
turns = []
for i in range(iterations):
    turns += [True] + [not turn for turn in turns[::-1]]

loc = np.array([0, 0])
facing = 'e'
walklen = 1
walkdir = {
    'n': np.array([0, 1]),
    'e': np.array([1, 0]),
    's': np.array([0, -1]),
    'w': np.array([-1, 0])
}
right = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
left = {'n': 'w', 'w': 's', 's': 'e', 'e': 'n'}

# iteration 0
points = [loc]
loc = loc + walkdir[facing]*walklen
points.append(loc)

# iterations > 0
for turn in turns:
    facing = right[facing] if turn else left[facing]
    loc = loc + walkdir[facing]*walklen
    points.append(loc)

for i in range(len(points)-1):
    x0, y0 = points[i]
    x1, y1 = points[i+1]
    plt.plot([x0, x1], [y0, y1], 'k')

plt.show()
