# imports
from dijkstar import Graph, find_path
from sys import maxsize

# main function
def main():
    # open file
    f = open("puzzle.txt", "r")
    heightmap = f.read().split('\n')
    heightmap = [list(line) for line in heightmap]

    # first, find start and end
    start, end = 0, 0
    for i, line in enumerate(heightmap):
        for j, curr_height in enumerate(line):
            n = i*len(line)+j
            if curr_height == 'S':
                start = n
                heightmap[i][j] = 'a'
            if curr_height == 'E':
                end = n
                heightmap[i][j] = 'z'

    # Create graph 
    graph = Graph()
    candidate_starts = []
    for i, line in enumerate(heightmap):
        for j, curr_height in enumerate(line):
            n = i*len(line) + j
            if i > 0 and ord(curr_height)+1 >= ord(heightmap[i-1][j]):
                graph.add_edge(n, n-len(line), 1)
            if j > 0 and ord(curr_height)+1 >= ord(heightmap[i][j-1]):
                graph.add_edge(n, n-1, 1)
            if i < len(heightmap)-1 and ord(curr_height)+1 >= ord(heightmap[i+1][j]):
                graph.add_edge(n, n+len(line), 1)
            if j < len(line)-1 and ord(curr_height)+1 >= ord(heightmap[i][j+1]):
                graph.add_edge(n, n+1, 1)

            # used in part 2
            if curr_height == 'a':
                candidate_starts.append(n)
    
    # now, find shortest path
    shortest_path = find_path(graph, start, end)
    print(shortest_path.total_cost)

    # now, we want to try all possible start positions, and determine the best path
    best = maxsize
    for c_start in candidate_starts:
        try:
            shortest_path = find_path(graph, c_start, end)
        except:
            continue
        else:
            length = shortest_path.total_cost
            if length < best:
                best = length
    print(best)

    # close file
    f.close()

if __name__ == "__main__":
    main()