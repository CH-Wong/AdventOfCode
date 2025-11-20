import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator


def str_to_num(string):
    return ord(string) - ord("a")

with open("input_day12.txt") as datafile:
    height_map = datafile.read().strip().split("\n")


height_map = np.array([[str_to_num(point) for point in row] for row in height_map])

start_height = str_to_num("S")
end_height = str_to_num("E")

start_nodes = []

G = nx.DiGraph()
for ypos, row in enumerate(height_map):
    for xpos, height in enumerate(row):
        if height == start_height or height == 0:
            start_nodes.append((xpos, ypos))
            height = str_to_num("a")
            height_map[ypos, xpos] = height
        
        elif height == end_height:
            end_node = (xpos, ypos)
            height = str_to_num("z")
            height_map[ypos, xpos] = height

        G.add_node((xpos, ypos), height=height)
        
for ypos, row in enumerate(height_map[:-1]):
    for xpos, height in enumerate(row[:-1]):
        current_height = G.nodes[(xpos, ypos)]["height"]

        target_height = G.nodes[(xpos + 1, ypos)]["height"]
        if xpos != len(row):
            if current_height - 1 <= target_height <= current_height + 1:
                G.add_edge((xpos + 1, ypos), (xpos , ypos))
                G.add_edge((xpos, ypos), (xpos + 1, ypos))
            
            elif target_height < current_height - 1:
                G.add_edge((xpos, ypos), (xpos + 1, ypos))

        target_height = G.nodes[(xpos, ypos + 1)]["height"]
        if ypos != len(height_map):
            if current_height - 1 <= target_height <= current_height + 1:
                G.add_edge((xpos, ypos + 1), (xpos , ypos))
                G.add_edge((xpos, ypos), (xpos, ypos + 1))
            
            elif target_height < current_height - 1:
                G.add_edge((xpos, ypos), (xpos, ypos + 1))
        
shortest_paths = []
path_lengths = []
for start_node in start_nodes:
    # print(f"Finding path from {start_node} to {end_node}")
    try:
        path = nx.dijkstra_path(G, start_node, end_node)
        shortest_paths.append(path)
        path_lengths.append(len(path))
        # print(path, len(path) - 1)

    except nx.exception.NetworkXNoPath:
        # print("No path found.")
        pass


print(min(path_lengths) - 1, start_nodes[path_lengths.index(min(path_lengths))])

X = np.arange(0, np.shape(height_map)[1])
Y = np.arange(0, np.shape(height_map)[0])
X, Y = np.meshgrid(X, Y)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Plot the surface.
surf = ax.plot_surface(X, Y, height_map, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False, alpha = 0.3)

x_vector = []
y_vector = []
z_vector = []
for node in shortest_paths[path_lengths.index(min(path_lengths))]:
    x_vector.append(node[0])
    y_vector.append(node[1])
    z_vector.append(G.nodes[node]["height"] + 1)

ax.plot3D(x_vector, y_vector, z_vector, 'black')

plt.show()