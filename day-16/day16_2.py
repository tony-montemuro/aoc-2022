import copy

# takes the list of valves, and converts the string valve types into numbers
def hash(v):
    for index, valve in enumerate(valves):
        if v == valve:
            return index
    return -1

# floyd warshall
def f_w(graph):
    dist = copy.deepcopy(graph)
    for k in range(v):
        # pick all vertices as source one by one
        for i in range(v):
            # Pick all vertices as destination for the above picked source
            for j in range(v):
                # If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

# open file
f = open("puzzle.txt", "r")
input = f.read().split('\n')
current_valve = "AA"
valves, flow_rates, tunnels = [], [], []
map = {}
start = None

# parse
for i, line in enumerate(input):
    line_arr = line.split(' ')
    valve = line_arr[1]
    if valve == 'AA':
        start = i
    valves.append(line_arr[1])
    flow_rates.append(int(line_arr[4].split('=')[1][:-1]))
    tunnels.append([line[:-1] if len(line) > 2 else line for line in line_arr[9:]])

# hash the valves and tunnels lists
for i, ts in enumerate(tunnels):
    for j, v in enumerate(ts):
        tunnels[i][j] = hash(v)
for i, v in enumerate(valves):
    valves[i] = hash(v)

# generate a graph matrix
v = len(valves)
inf = 99999
graph = [[0] * v for i in range(0, v)]
for y, row in enumerate(graph):
    for x, column in enumerate(row):
        l = tunnels[y]
        for valve in l:
            graph[y][valve] = 1
for y, row in enumerate(graph):
    for x, column in enumerate(row):
        if y != x and column == 0:
            graph[y][x] = inf
f_w_graph = f_w(graph)

# get the list of all nodes whose flow rate is greater than zero
important = []
for i, fr in enumerate(flow_rates):
    if fr > 0:
        important.append(i)

# create new graph
compressed = {}
for line_num, line in enumerate(f_w_graph):
    d = {}
    for i in important:
        if line_num != i:
            d[i] = f_w_graph[line_num][i]
    compressed[line_num] = d

# create dictionaries and lists
v_dict = {}
for i in valves:
    v_dict[i] = flow_rates[i]
indicies = {}
for i, e in enumerate(important):
    indicies[e] = i

# define a dfs function with dynamic programming
cache = {}
def traverse(bitmask, time, valve):
    if (bitmask, time, valve) in cache:
        return cache[(bitmask, time, valve)]

    maximum = 0
    for other in compressed[valve]:
        bit = 1 << indicies[other]
        if bitmask & bit:
            continue
        time_remaining = time-compressed[valve][other]-1
        if time_remaining <= 0:
            continue
        maximum = max(maximum, traverse(bitmask|bit, time_remaining, other) + v_dict[other]*time_remaining)
    
    cache[(bitmask, time, valve)] = maximum
    return maximum

# part 2 answer
begin = (1 << len(important)) - 1
m = 0
for i in range((begin+1) // 2):
    m = max(m, traverse(i, 26, start)+traverse(begin^i, 26, start))
print(m)