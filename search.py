graph = { 
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': ['H', 'I'],
            'E': ['J', 'K'],
            'F': ['L', 'M'],
            'G': ['N', 'O'],
            'initial': ['A'],
            'goal': 'L'
        }

def general_search(problem, queuing_fn):
    solution = []
    nodes = problem['initial'][:]   # weird python: to copy do slicing
    while nodes:
        node = nodes.pop(0)
        solution.append(node)
        if node == problem['goal']:
            return solution

        nodes = queuing_fn(problem, node, nodes)


    raise Exception("No solution!")


def breadth_first_search(problem, node, nodes):
    if node in problem.keys():
        nodes.extend(problem[node]) # FIFO

    return nodes


def depth_first_search(problem, node, nodes):
    if node in problem.keys():
        nodes[0:0] = problem[node] # STACK

    return nodes

print "solution: " + str(general_search(graph, breadth_first_search))

print "solution: " + str(general_search(graph, depth_first_search))
