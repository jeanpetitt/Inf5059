from collections import deque

# construct the graph
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        """add an adge between two nodes (places)."""
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)  #Graph not orientef

    def display(self):
        """display the graph."""
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")
            
def bfs(graph, start):
    """
    visit BFS (BreadBreadth-First) of a graph.
    :param graph: dict that represent the graph
    :param start: start node
    :return: list of node visited
    """
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])  # Add neighbors not visited
    
    return result

def dfs_recursive(graph, node, visited=None, result=None):
    """
    visit DFS (Deep first) recursif.
    :param graph: Dict that represent the graph.
    :param node: Actual node.
    :param visited: set of not visited
    :param result: List of visited nodes
    :return: List of visited nodes
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []
    if node not in visited:
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited, result)

    return result

def dfs_iterative(graph, start):
    """
    visit DFS (Deep first) with a stack.
    :param graph: Dict that represent the graph
    :param start: first node
    :return: list of node visited
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(graph[node])  # add neighbors in the stack

    return result


def shortest_path_bfs(graph, start, target):
    """
    Find the shortest path between two nodes with BFS.
    :param graph: Dict that represent the graph
    :param start: start node
    :param target: target node
    :return: shortest path court or None
    """
    if start not in graph or target not in graph:
        return None
    
    queue = deque([(start, [start])])  # (Node, path)
    visited = set()

    while queue:
        node, path = queue.popleft()
        
        if node == target:
            return path  # Retourn the path found
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

    return None  # If we don't have connexion found

# Grapg graphe that reprsent a short map of yaounde city
city_map = Graph()
edges = [
    ("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), 
    ("D", "F"), ("E", "F"), ("E", "G"), ("F", "G")
]

for edge in edges:
    city_map.add_edge(*edge)

# Diplay graoh
print("Graph that reprsent the city:")
print(f"A=Mimbomane, B=Terminus, C=Post, D=Mobile Essos, E=Camer F=Omnisport, G=Titi garage")
city_map.display()

# Test BFS et DFS
print("\nBFS From A:", bfs(city_map.graph, "A"))
print("DFS (recursif) from A:", dfs_recursive(city_map.graph, "A"))
print("DFS (iterative) from A:", dfs_iterative(city_map.graph, "A"))

# check connectivity  and search of the shorted path
print("\nThe shortest path between A et G:", shortest_path_bfs(city_map.graph, "A", "G"))
print("The shortest path between B et E:", shortest_path_bfs(city_map.graph, "B", "E"))
print("The shortest path between D et G:", shortest_path_bfs(city_map.graph, "D", "G"))
print("The shortest path between A et X:", shortest_path_bfs(city_map.graph, "A", "X"))  # Test with node does not exist