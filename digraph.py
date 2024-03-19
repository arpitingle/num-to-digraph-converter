import networkx as nx
import matplotlib.pyplot as plt

def create_digraph_from_string(string):
    # Create an empty directed graph
    G = nx.DiGraph()

    # Convert the string into a list of numbers
    numbers = [int(string[i]) for i in range(len(string))]

    # Add nodes to the graph
    for num in numbers:
        G.add_node(num)

    # Add directed edges between consecutive numbers
    for i in range(len(numbers) - 1):
        G.add_edge(numbers[i], numbers[i + 1])

    return G

# Example usage
input_string = "170603762"
digraph = create_digraph_from_string(input_string)

# Plot the digraph
nx.draw(digraph, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, arrowsize=20)
plt.title("Directed Graph from Continuous String of Numbers")
plt.show() 
