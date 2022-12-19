# imports
from math import floor

# global variables
max = None
total_time = 30
valve_map = {}
state_map = {}

# function that will simulate pipe traversal (part 1)
def traverse(opened, current_valve, pressure, time):
    global max
    global total_time

    # base case: we have finish traversing this path. if the pressure is greater than max,
    # update pressure, and return max. otherwise, return -1
    if time == total_time:
        if pressure > max:
            max = pressure
            return max
        return -1

    # general case
    # first, we want to determine if a path is not worth exploring. to do this,
    # we need to get the (time_remaining / 2) unopened valves (or just the
    # remaining unopened valves if there are less than (time_remaining / 2 left))
    # simulate opening each one in the best order. if the pressure from this simulation
    # summed with the pressure is still less than max, this is a bad path. return -1.
    time_remaining = total_time-time
    i, new_pressure, target = 0, 0, floor(time_remaining/2)
    all_valves, unopened = list(valve_map.keys()), []
    while i < len(all_valves) and len(unopened) < target:
        if all_valves[i] not in opened:
            new_pressure += ((time_remaining-2*len(unopened))*valve_map[all_valves[i]][0])
            unopened.append(all_valves[i])
        i += 1

    if pressure + new_pressure < max:
        return -1

    fr = valve_map[current_valve][0]
    possible_valves = valve_map[current_valve][1]
    # if current valve has not been opened, and flow rate is non-zero, we want
    # to try all paths with it closed AND open
    if current_valve not in opened and fr > 0:
        # edge case: time = total_time-1.
        if time == total_time-1:
            return traverse(opened, current_valve, pressure+fr, time+1)

        # general case: time < total_time-1
        r = -1
        for v in possible_valves:
            val = traverse(opened, v, pressure, time+1)
            r = val if val > r else r
        for v in possible_valves:
            val = traverse(opened+[current_valve], v, pressure+((total_time-time)*fr), time+2)
            r = val if val > r else r
        return r
    else:
        r = -1
        for v in possible_valves:
            val = traverse(opened, v, pressure, time+1)
            r = val if val > r else r
        return r

# function that should give us a decently high max before we
# begin traversing more paths (part 1)
def init_traverse(valve):
    # approach: when choosing a valve to traverse, pick the valve not yet visited
    # if possible
    global valve_map
    global total_time
    opened = set()
    opened.add('AA')
    time, pressure = 1, 0
    while time < total_time:
        # minute one
        possible_valves = valve_map[valve][1]
        next_v = None
        for v in possible_valves:
            if v not in opened:
                next_v = v
        if next_v is None:
            next_v = possible_valves[0]
        time += 1

        # minute two
        if next_v not in opened:
            pressure += (total_time-time)*valve_map[next_v][0]
        opened.add(next_v)
        valve = next_v
        time += 1
    return pressure

# main function
def main():
    # open file
    f = open("puzzle.txt", "r")
    input = f.read().split('\n')
    current_valve = "AA"
    map = {}

    # parse
    global valve_map
    for line in input:
        line_arr = line.split(' ')
        valve = line_arr[1]
        flow_rate = int(line_arr[4].split('=')[1][:-1])
        other_valves = [line[:-1] if len(line) > 2 else line for line in line_arr[9:]]
        map[valve] = (flow_rate, other_valves)

    # sort valve_map based on the flow rate
    valve_map_list = sorted(map.items(), key=lambda x: x[1][0], reverse=True)
    for v in valve_map_list:
        valve_map[v[0]] = v[1]

    # now, we are going to do a simple traversal of the graph, which will get us a high
    # max before we begin traversing all possible path
    global max
    max = init_traverse(current_valve)
    
    # traverse pipe system to determine best possible valve layout
    time, pressure = 1, 0
    opened = []
    max_pressure = traverse(opened, current_valve, pressure, time)
    
    # answer to part 1
    print(max_pressure)

    # close file
    f.close()

if __name__ == "__main__":
    main()