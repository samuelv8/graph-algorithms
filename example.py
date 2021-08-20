import networkx as nx


def get_example():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 4), (1, 5), (2, 3), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 8), (6, 7), (7, 8)])

    G = {
        'graph': G,
        'pos': {1: (0, 0), 2: (0, 3), 3: (3, 3), 4: (3, 0), 5: (1, 1), 6: (1, 2), 7: (2, 2), 8: (2, 1)},
        'options': {
            "font_size": 22,
            "node_size": 1000,
            "node_color": "white",
            "edgecolors": "black",
            "linewidths": 5,
            "width": 5,
        }
    }

    H = nx.Graph()
    H.add_edges_from([(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 8), (3, 5), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8)])

    H = {
        'graph': H,
        'pos': {1: (0, 0), 2: (0, 3), 3: (3, 3), 4: (3, 0), 5: (1, 1), 6: (1, 2), 7: (2, 2), 8: (2, 1)},
        'options': {
            "font_size": 22,
            "node_size": 1000,
            "node_color": "white",
            "edgecolors": "black",
            "linewidths": 5,
            "width": 5,
        }
    }

    return G, H

G, H = get_example()
print(G)
