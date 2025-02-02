def reconstruct_path(graph, start, end, distances):
    """
      Reconstruit le chemin le plus court en utilisant les informations du BFS.

    Args:
        graph (dict): Représentation du graphe sous forme de dictionnaire.
                    Les clés sont les nœuds et les valeurs sont les listes de leurs voisins.
        start : Le nœud de départ du chemin.
        end : Le nœud de destination du chemin.
        distances (dict) : Distances calculées par BFS.

    Returns:
         list: Le chemin le plus court sous forme de liste de nœuds.
    """
    path = [end]  # Commence le chemin par la destination
    current_node = end
    while current_node != start:
        found_previous = False
        for neighbor in graph[current_node]:
            if distances[neighbor] == distances[current_node] - 1:
                path.insert(0, neighbor) # Ajoute le nœud au début du chemin
                current_node = neighbor
                found_previous = True
                break # On arrête dès qu'on a trouvé le nœud précédent
        if not found_previous: #Si il y a une erreur, on arrête pour éviter une boucle infinie
             print("Erreur lors de la reconstruction du chemin le plus court.")
             return []
    return path