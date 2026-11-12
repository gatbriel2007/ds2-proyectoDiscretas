from graph import   DirectedGraph, UndirectedGraph
from collections import deque

def load_graph(file_path: str, is_directed: bool = False):

    graph = DirectedGraph() if is_directed else UndirectedGraph()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            source = parts[0].strip()
            target = parts[1].strip()
            weight = float(parts[2].strip())

            graph.add_edge(source, target, weight)

    return graph

def is_connected(graph) -> bool:
    nodes = graph.get_nodes()

    if len(nodes) <= 1:
        print("is_connected: True")
        return True

    start_node = nodes[0]
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        current = queue.popleft()
        neighbors = graph.adj.get(current, [])
        for neighbor, weight in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    result = len(visited) == len(nodes)
    print(f"is_connected: {result}")
    return result

def has_cycles(graph) -> bool:
    nodes = graph.get_nodes()
    visited = set()

    for start_node in nodes:
        if start_node not in visited:
            queue = deque([(start_node, None)])
            visited.add(start_node)

            while queue:
                current, parent = queue.popleft()
                neighbors = graph.adj.get(current, [])

                for neighbor, weight in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)

                        queue.append((neighbor, current))
                    elif neighbor != parent:
                        print("has_cycles: True")
                        return True
    print("has_cycles: False")
    return False

if __name__ == "__main__":

    with open("test_connected.txt", "w", encoding="utf-8") as f:
        f.write("A, B, 5\n")
        f.write("B, C, 3\n")
        f.write("C, A, 2\n")

    graph_connected = load_graph(
        "test_connected.txt", is_directed=False
    )
    print("--- Test 1 (connected graph) ---")
    is_connected(graph_connected)

    with open("test_disconnected.txt", "w", encoding="utf-8") as f:
        f.write("A, B, 5\n")
        f.write("C, D, 2\n")

    graph_disconnected = load_graph(
        "test_disconnected.txt", is_directed=False
    )
    print("\n--- Test 2 (disconnected graph) ---")
    is_connected(graph_disconnected)

    print("\ntest vertex:", graph_connected.get_nodes())
    print("Adjacency list:", graph_connected.adj)

    with open("test_cycle.txt", "w", encoding="utf-8") as f:
        f.write("A, B, 5\n")
        f.write("B, C, 3\n")
        f.write("C, A, 2\n")

    graph_cycle = load_graph("test_cycle.txt", is_directed=False)
    print("\n--- test 1 (cycle graph) ---")
    has_cycles(graph_cycle)

    with open("test_no_cycle.txt", "w", encoding="utf-8") as f:
        f.write("A, B, 5\n")
        f.write("B, C, 3\n")

    graph_no_cycle = load_graph(
        "test_no_cycle.txt", is_directed=False
    )
    print("\n--- test 2 (no cycle graph) ---")
    has_cycles(graph_no_cycle)