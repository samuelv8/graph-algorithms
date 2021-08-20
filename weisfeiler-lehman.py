import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter


def weisfeiler_lehman_iter(G: nx.Graph):
    # Iterando em cada nó e verificando o label dos vizinhos
    mset = {}
    for node in G.nodes:
        mset[node] = Counter()  # python built-in type for multisets
        for ng in G[node]:
            mset[node][G.nodes[ng]['label']] += 1

    # Iterando pelos multisets criados e fazendo o hash
    for node in G.nodes:
        mset[node] = hash(frozenset(mset[node].items()))  # frozenset allows to hash dict obj

    # Atribuindo novo label para cada nó
    for node in G.nodes:
        G.nodes[node]['label'] = mset[node]

    return Counter(mset.values())


def check_equal(G: nx.graph, H: nx.graph):
    return sorted(G.nodes) == sorted(H.nodes)


def weisfeiler_lehman_test(G: nx.Graph, H: nx.Graph, k: int):
    """
    Applies the Weisfeiler-Lehman isomorphism test between two graphs.
    :param G: First graph
    :param H: Second graph
    :param k: Iteration limit
    :return: True if it passed the test in k iterations or False if don't
    """
    # Sanity check
    if len(G.nodes) != len(H.nodes) | len(G.edges) != len(G.edges):
        return False

    # Atribuindo os graus como labels iniciais
    for node in G.nodes:
        G.nodes[node]['label'] = G.degree[node]

    for node in H.nodes:
        H.nodes[node]['label'] = H.degree[node]

    # Iterações do teste de Weisfeiler-Lehman
    c = []
    for i in range(k):
        new_c = weisfeiler_lehman_iter(G)
        weisfeiler_lehman_iter(H)
        if check_equal(G, H):
            new_c = sorted(list(new_c.values()))
            if new_c == c:
                # Stops iterating if the label's configuration hasn't changed
                break
            else:
                c = new_c
                continue
        else:
            return False

    return True


if __name__ == '__main__':
    pass

# Test
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 4), (1, 5), (2, 3), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 8), (6, 7), (7, 8)])

H = nx.Graph()
H.add_edges_from([(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 8), (3, 5), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8)])

print(weisfeiler_lehman_test(G, H, 10))

# Print graphs

# explicitly set positions
pos = {1: (0, 0), 2: (0, 3), 3: (3, 3), 4: (3, 0), 5: (1, 1), 6: (1, 2), 7: (2, 2), 8: (2, 1)}

options = {
    "font_size": 22,
    "node_size": 1000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()

pos = {1: (0, 3), 2: (0, 2), 3: (0, 1), 4: (0, 0), 5: (1, 3), 6: (1, 2), 7: (1, 1), 8: (1, 0)}
nx.draw_networkx(H, pos, **options)

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
