from graph_algorithms import bfs, dfs, are_connected

# Exemple de graphe (non orienté)
example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': ['E', 'F'],
    'E': ['D', 'F'],
    'F': ['D', 'E'],
    'G': ['H'],
    'H': ['G']
}


def display_graph(graph):
  """
    Affiche la représentation du graphe à l'utilisateur
    Args:
         graph (dict): Representation of the graph
  """
  print("Représentation du graphe:")
  for node, neighbors in graph.items():
       print(f"   {node} : {', '.join(neighbors)}")
  print()


def get_valid_node(prompt, graph):
    """
    Demande à l'utilisateur d'entrer un nœud valide du graphe et gère les entrées erronées.
    Args:
        prompt (str) : Message à afficher à l'utilisateur.
        graph (dict) : Representation of the graph.
    Returns:
        str : Noeud valide saisi par l'utilisateur.
    """
    while True:
         try :
            node = input(prompt).upper()
            if node in graph: # Vérifie si le noeud est dans le graphe
                return node
            else:
                print(f"Erreur: Veuillez entrer un noeud valide du graphe, comme {', '.join(graph.keys())}")
         except ValueError:
            print("Erreur : Veuillez entrer un noeud valide.")
         except :
             print("Erreur : Veuillez entrer un noeud valide.")

def main():
    """
    Fonction principale pour interagir avec l'utilisateur, exécuter BFS, DFS,
    la vérification de connectivité, permettre la répétition des explorations et gérer les erreurs de saisie.
    """
    print("Bienvenue dans le programme de parcours de graphes!\n")
    display_graph(example_graph) # Affiche le graphe à l'utilisateur

    while True: # Boucle pour permettre des explorations multiples

        # Demander à l'utilisateur un noeud de départ valide pour BFS
        start_node_bfs = get_valid_node("Entrez le nœud de départ pour BFS (par exemple, A) : ", example_graph)
        print("\nRésultats de BFS:")
        distances = bfs(example_graph, start_node_bfs)
        print("\nDistances à partir du nœud",start_node_bfs," :")
        for node, dist in distances.items():
            print(f"   {node} : {dist}")
        print() # New line for readability

        # Demander à l'utilisateur un noeud de départ valide pour DFS
        start_node_dfs = get_valid_node("Entrez le nœud de départ pour DFS (par exemple, A) : ",example_graph)
        print("\nRésultats de DFS:")
        visited_nodes = dfs(example_graph, start_node_dfs)
        print("\nNœuds visités par DFS à partir de", start_node_dfs," :", visited_nodes)
        print() # New line for readability

        # Demander à l'utilisateur deux noeuds valides pour vérifier la connectivité
        node1 = get_valid_node("Entrez le premier nœud pour vérifier la connexion (par exemple, A): ", example_graph)
        node2 = get_valid_node("Entrez le deuxième nœud pour vérifier la connexion (par exemple, F): ", example_graph)

        are_connected_result, shortest_path  = are_connected(example_graph, node1, node2)
        if are_connected_result:  # Affiche un message approprié si ils sont connectés
            print(f"\nLes nœuds {node1} et {node2} sont connectés.  Chemin le plus court : {shortest_path}")
        else:  # Affiche un message approprié si ils ne sont pas connectés
            print(f"\nLes nœuds {node1} et {node2} ne sont pas connectés.")
        print()  # New line for readability

        # Demander à l'utilisateur s'il veut continuer
        continue_exploration = input("Voulez-vous effectuer une autre exploration du graphe ? (oui/non) : ").lower()
        if continue_exploration != "oui":
            print("\nAu revoir!")
            break # Sort de la boucle si l'utilisateur ne souhaite pas continuer
        print()  # New line for readability

if __name__ == "__main__":
    main()