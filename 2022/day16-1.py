import re
import networkx as nx
import matplotlib.pyplot as plt

with open("input_day16_example.txt") as datafile:
    data = datafile.read().strip().split("\n")

regex = "Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? ([\S\s]+)"

valves = {}

for line in data:
    current_valve, flow_rate, target_valves = re.match(regex, line).groups()

    if "," in target_valves:
        target_valves = target_valves.split(", ")
    else:
        target_valves = [target_valves]

    valves[current_valve] = {"targets": target_valves, "flow_rate": int(flow_rate), "state": False}

G = nx.Graph()
print("Adding valves")
for node, properties in valves.items():
    G.add_node(node, flow_rate = properties["flow_rate"], state=properties["state"])

print("Adding tunnels")
for source, properties in valves.items():
    for target in properties["targets"]:
        G.add_edge(source, target)

pressure_release = 0

# for flow_rate, state in zip(nx.get_node_attributes(G, "flow_rate").values(), nx.get_node_attributes(G, "open").values()):
#     if state:
#         pressure_release += flow_rate

def highest_value_valve(source, valves: dict):
    values = []
    paths = []
    for target, properties in valves.items():
        if not properties["state"]:
            value, path = get_value(source, target, valves)
            paths.append(path)
            values.append(value)
    
    max_index = values.index(max(values))
    
    return values[max_index], paths[max_index]


def get_value(source, target, valves):
    path = nx.shortest_path(G, source, target)
    return valves[target]["flow_rate"]/len(path), path

def get_next_target(source, max_length, valves:dict, depth=0):
    if depth == 0:
        return highest_value_valve(source, valves)
    
    elif depth > 0:
        values = []
        paths = []

        for target, properties in valves.items():
            if not properties["state"]:
                new_valves = valves.copy()
                new_valves[target]["state"] = True

                value_t, path_t = get_value(source, target, valves)

                value, path = get_next_target(target, new_valves, depth=depth-1)

                if len(path) < max_length:
                    print(value_t, value)
                    values.append(value_t + value)
                    paths.append(path_t)

        
        max_index = values.index(max(values))
        return values[max_index], paths[max_index]

starting_node = "AA"
path=[starting_node]
max_duration = 30

walking = True
while walking:
    if len(path) >= max_duration + 1:
        walking = False
        continue

    possible_targets = {valve: properties["flow_rate"] for valve, properties in valves.items() if properties["flow_rate"] == 0 or not properties["state"]} 
    
    effect = []
    shortest_paths = []
    for target, flow_rate in possible_targets.items():
        shortest_path = nx.shortest_path(G, path[-1], target)
        shortest_paths.append(shortest_path)
        val, path_to_next = highest_value_valve(target, valves)

        # add 1 extra to account for opening valve
        if len(path) + len(shortest_path) >= max_duration + 1:
            effect.append(0)
            continue
        else:
            effect.append(flow_rate / (len(shortest_path) + len(path_to_next)))
    
    print(path, "--------------------------")
    for e, p in zip(effect, shortest_paths):
        print(e, p)

    if all([x == 0 for x in effect]):
        print("Ran out of possible destinations. Terminating run.")
        walking = False
        continue


    path += shortest_paths[effect.index(max(effect))][1:]
    path += [path[-1]]

    valves[path[-1]]["state"] = True

for valve, properties in valves.items():
    print(valve, properties["flow_rate"], properties["state"])

print(len(path), path)

pressure_release = 0
prev_node = None
for t, node in enumerate(path):
    print(prev_node, node)
    if prev_node == node:
        pressure_release += (max_duration - t) * valves[node]["flow_rate"]
        print(node, t, (max_duration - t) * valves[node]["flow_rate"])
    prev_node = node


print(pressure_release)


pos = nx.spring_layout(G)
nx.draw_networkx_labels(G, pos)
nx.draw(G, pos)
plt.show()