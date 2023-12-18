import math
from heapq import *

def find_minimum_heat_loss(heat_map):
    """Ooooh, this is my first time using Dijkstra"""
    # dictionary keys need to include position,
    # direction,
    # and number of steps in a straight line to get there
    result_map = {}
    for x in range(len(heat_map[0])):
        for y in range(len(heat_map)):
            for direction in "NESW":
                for steps in range(1,4):
                    result_map[((x,y), direction, steps)] = math.inf

    result_map[((0,0), "E", 1)] = 0
    result_map[((0,0), "S", 1)] = 0
    
    visited = set()
    
    queue = []
    for n in result_map:
        heappush(queue, (result_map[n], n))
    
    direction_coords = {"N": (0,-1), "E": (1,0), "S":(0,1), "W":(-1,0)}
    directions = {"N": "NEW", "E": "NES", "S": "ESW", "W": "NSW"}
    
    while queue:
        # find adjacent nodes
        current_distance, current_node = heappop(queue)
        
        adjacent_nodes = []
        for direction in directions[current_node[1]]:
            x = current_node[0][0] + direction_coords[direction][0]
            y = current_node[0][1] + direction_coords[direction][1]
            if current_node[1] != direction:
                node = ((x,y), direction, 1)
                if node not in visited and node in result_map:
                    adjacent_nodes.append(node)
            elif current_node[2] < 3:
                node = ((x,y), direction, current_node[2] + 1)
                if node not in visited and node in result_map:
                    adjacent_nodes.append(node)

        for node in adjacent_nodes:
            x, y = node[0]
            distance = current_distance + heat_map[y][x]
            if distance < result_map[node]:
                result_map[node] = distance
                heappush(queue, (distance, node))

        visited.add(current_node)

    return min(v for k, v in result_map.items() if k[0] == (len(heat_map[0]) - 1, len(heat_map) - 1))

def part_two(heat_map):
    """Ooooh, this is my second time using Dijkstra"""
    result_map = {}
    for x in range(len(heat_map[0])):
        for y in range(len(heat_map)):
            for direction in "NESW":
                for steps in range(1,11):
                    result_map[((x,y), direction, steps)] = math.inf
                    
    result_map[((0,0), "E", 1)] = 0
    result_map[((0,0), "S", 1)] = 0

    visited = set()
    queue = []
    for n in result_map:
        heappush(queue, (result_map[n], n))

    direction_coords = {"N": (0,-1), "E": (1,0), "S":(0,1), "W":(-1,0)}
    directions = {"N": "NEW", "E": "NES", "S": "ESW", "W": "NSW"}

    while queue:
        current_distance, current_node = heappop(queue)
        
        adjacent_nodes = []
        for direction in directions[current_node[1]]:
            x = current_node[0][0] + direction_coords[direction][0]
            y = current_node[0][1] + direction_coords[direction][1]
            if current_node[1] != direction:
                node = ((x,y), direction, 1)
                if node not in visited and node in result_map and current_node[2] >= 4:
                    adjacent_nodes.append(node)
            else:
                node = ((x,y), direction, current_node[2] + 1)
                if node not in visited and current_node[2] <= 9 and node in result_map:
                    adjacent_nodes.append(node)
        
        for node in adjacent_nodes:
            x, y = node[0]
            distance = current_distance + heat_map[y][x]
            if distance < result_map[node]:
                result_map[node] = distance
                heappush(queue, (distance, node))

        visited.add(current_node)
        
    valid_nodes = {k: v for k, v in result_map.items() if k[0] == (len(heat_map[0]) - 1, len(heat_map) - 1)}
    valid_nodes = {k: v for k, v in valid_nodes.items() if k[2] >= 4}
    return min(valid_nodes.values())

if __name__ == "__main__":
    with open("inputs/day_17.txt") as f:
        heat_map = f.read().splitlines()
        heat_map = [[int(x) for x in list(r)] for r in heat_map]
        min_heat_loss = find_minimum_heat_loss(heat_map)
        print(min_heat_loss, "< min heat loss")
        ultra_heat_loss = part_two(heat_map)
        print(ultra_heat_loss, "< ultra heat loss")
