from collections import deque
from graph_utils import reconstruct_path

def bfs(graph, start_node):
    """
    Parcours un graphe en largeur (BFS).

    Args:
        graph (dict): Représentation du graphe sous forme de dictionnaire.
                      Les clés sont les nœuds et les valeurs sont les listes de leurs voisins.
        start_node : Le nœud de départ pour le parcours.

    Returns:
        dict : Un dictionnaire des nœuds visités et leur distance par rapport au nœud de départ.
    """
    visited = {node: False for node in graph}  # Dictionnaire pour suivre les nœuds visités
    distances = {node: float('inf') for node in graph}  # Dictionnaire pour suivre la distance par rapport au nœud de départ
    queue = deque([start_node]) # File d'attente pour les nœuds à explorer
    visited[start_node] = True  # Marquer le nœud de départ comme visité
    distances[start_node] = 0  # La distance du nœud de départ à lui-même est 0

    while queue:
        current_node = queue.popleft()  # On retire le nœud actuel de la file
        print(f"Visite du nœud : {current_node}")  # Afficher le nœud visité

        for neighbor in graph[current_node]:  # On parcours les voisins du nœud
            if not visited[neighbor]:  # Si le voisin n'est pas visité
                visited[neighbor] = True   # Marquer le voisin comme visité
                distances[neighbor] = distances[current_node]+1  # Calcul de la distance par rapport au noeud de départ
                queue.append(neighbor)  # Ajouter le voisin dans la file d'attente à traiter

    return distances

def dfs(graph, start_node, visited=None):
    """
    Parcours un graphe en profondeur (DFS) de manière récursive.

    Args:
        graph (dict): Représentation du graphe sous forme de dictionnaire.
                      Les clés sont les nœuds et les valeurs sont les listes de leurs voisins.
        start_node : Le nœud de départ pour le parcours.
        visited (set) : Ensemble pour suivre les nœuds visités (récursif)

    Returns:
        set: Ensemble des nœuds visités lors du parcours.
    """
    if visited is None:
        visited = set()  # Ensemble pour suivre les nœuds visités (initialisation)

    visited.add(start_node) # Marquez le nœud actuel comme visité

    print(f"Visite du nœud : {start_node}") # Afficher le nœud visité

    for neighbor in graph[start_node]:  # On parcours les voisins du nœud
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Appel récursif pour visiter le voisin
    return visited


def are_connected(graph, node1, node2):
    """
    Vérifie si deux nœuds sont connectés dans un graphe et trouve le chemin le plus court avec BFS.

    Args:
        graph (dict) : Représentation du graphe sous forme de dictionnaire.
                      Les clés sont les nœuds et les valeurs sont les listes de leurs voisins.
        node1 : Le premier nœud.
        node2 : Le second nœud.

    Returns:
        bool, list : Un booléen indiquant si les nœuds sont connectés, et le chemin le plus court.
    """
    distances = bfs(graph, node1)  # On utilise BFS pour obtenir les distances

    if distances[node2] == float('inf'):  # Si la distance vers node2 est infinie, ils ne sont pas connectés
        return False, []
    else:
        # Reconstruction du chemin le plus court
        shortest_path = reconstruct_path(graph, node1, node2, distances)
        return True, shortest_path