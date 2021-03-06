import matplotlib.pyplot as plt
import networkx as nx
import re, string

def main():
    web = Connection_Web()
    graph = web.build_graph("connections")
    web.draw_graph(graph)

'''
Displays a built graph from a data file of connections with
networkx and matplotlib.
'''
class Connection_Web():
    '''
    Builds and returns a graph based on the input file: file_name.
    '''
    def build_graph(self, file_name):
        graph = []
        with open(file_name, 'r') as file:
            for line in file:
                line = line.rstrip() # strip newline characters
                l = re.split("[,;:]", line) # split at punct
                cons = l[1:]
                for c in cons:
                    graph.append((l[0].strip(), c.strip()))
        return graph

    '''
    Takes a graph as a list of tuples for connections and draws it in matplotlib.
    '''
    def draw_graph(self, graph):
        nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
        G = nx.Graph()

        for node in nodes:
            G.add_node(node)

        for edge in graph:
            G.add_edge(edge[0], edge[1])

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, font_size=8)

        plt.axis("off")
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
        plt.show()

if __name__ == "__main__":
    main()
