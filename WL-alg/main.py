import networkx as nx


def weisfeiler_lehman_test(G, H):
    # Sanity check
    if len(G.nodes) != len(H.nodes) or len(G.edges) != len(G.edges):
        return False

    label_G = {}
    label_H = {}

    for node in G.nodes:
        G[node]['label'] = G.degree[node]





if __name__ == '__main__':
    pass


# Test
G = nx.Graph()
# G.add_nodes_from(range(8))
G.add_edges_from([(1, 2), (1, 4), (1, 5), (2, 3), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 8), (6, 7), (7, 8)])

H = nx.Graph()
G.add_edges_from([(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 8), (3, 5), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8)])

weisfeiler_lehman_test(G,H)