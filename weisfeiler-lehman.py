import networkx as nx


def weisfeiler_lehman_test(G, H):
    # Sanity check
    if len(G.nodes) != len(H.nodes) | len(G.edges) != len(G.edges):
        return False

    # Atribuindo os graus como labels iniciais
    for node in G.nodes:
        G.nodes[node]['label'] = G.degree[node]
        print(G.nodes[node])

    for node in H.nodes:
        H.nodes[node]['label'] = H.degree[node]

    return True


if __name__ == '__main__':
    pass


# Test
G = nx.Graph()
G.add_nodes_from(range(1, 8))
G.add_edges_from([(1, 2), (1, 4), (1, 5), (2, 3), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 8), (6, 7), (7, 8)])

H = nx.Graph()
H.add_edges_from([(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 8), (3, 5), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8)])

print(weisfeiler_lehman_test(G, H))