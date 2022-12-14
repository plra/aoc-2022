import networkx as nx
from p1 import build_graph

if __name__ == "__main__":
    G = build_graph("input.txt")
    min_steps = 2**63
    for node, height in G.nodes(data="height"):
        if height == 0:
            try:
                n_steps = nx.shortest_path_length(G, source=node, target=G.graph["end"])
                min_steps = min(min_steps, n_steps)
            except nx.NetworkXNoPath:
                pass
    print(min_steps)
