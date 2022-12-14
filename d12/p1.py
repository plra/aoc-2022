import networkx as nx


def build_graph(filename):
    with open(filename) as f:
        G = nx.DiGraph()
        # Nodes
        for i, line in enumerate(f):
            for j, ch in enumerate(line.strip()):
                if ch == "S":
                    G.graph["start"] = (i, j)
                    ch = "a"
                elif ch == "E":
                    G.graph["end"] = (i, j)
                    ch = "z"
                height = ord(ch) - ord("a")
                G.add_node((i, j), height=height)
        # Edges
        for u in G.nodes:
            i, j = u
            for v in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if v in G.nodes and G.nodes[v]["height"] - G.nodes[u]["height"] <= 1:
                    G.add_edge(u, v)
        return G


if __name__ == "__main__":
    G = build_graph("input_0.txt")
    n_steps = nx.shortest_path_length(G, source=G.graph["start"], target=G.graph["end"])
    print(n_steps)
