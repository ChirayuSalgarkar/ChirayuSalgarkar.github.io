#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    # Create an adjacency list
    adjacency_list = {i: [] for i in range(node_count)}
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # Initialize color assignment array
    colors = [-1] * node_count
    
    # Assign the first color to the first vertex
    colors[0] = 0
    
    # A temporary array to store the available colors. Initially, all colors are available.
    available = [False] * node_count
    
    # Assign colors to remaining vertices
    for u in range(1, node_count):
        # Process all adjacent vertices and mark their colors as unavailable
        for v in adjacency_list[u]:
            if colors[v] != -1:
                available[colors[v]] = True
        
        # Find the first available color
        cr = 0
        while cr < node_count and available[cr]:
            cr += 1
        
        # Assign the found color
        colors[u] = cr
        
        # Reset the values back to false for the next iteration
        for v in adjacency_list[u]:
            if colors[v] != -1:
                available[colors[v]] = False
    
    # The number of colors used
    obj = max(colors) + 1
    opt = 0  # Assuming we are not proving optimality
    
    # prepare the solution in the specified output format
    output_data = str(obj) + ' ' + str(opt) + '\n'
    output_data += ' '.join(map(str, colors))

    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')
