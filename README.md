# Algorithmes pour la Résolution de Problèmes et l'Optimisation

Ce dépôt GitHub contient le code source et la documentation pour un ensemble de cinq algorithmes fondamentaux en informatique et en ingénierie logicielle. Ces algorithmes ont été implémentés et testés dans le cadre du cours "Search Based Software Engineering".

## Contenu du Dépôt

Le dépôt est organisé comme suit :

*   **`binary_search_interactive.py`** :
    *   Implémentation interactive de l'algorithme de recherche binaire.
    *   Permet à l'utilisateur d'entrer une liste triée et une valeur cible.
    *   Affiche l'index de la cible si elle est trouvée, ou -1 si elle ne l'est pas.
*   **`graph_algorithms.py`** :
    *   Contient les implémentations des algorithmes de parcours de graphes : BFS et DFS.
    *   Contient la fonction `are_connected` pour vérifier la connectivité entre deux nœuds.
*   **`graph_utils.py`** :
    *   Contient des fonctions utilitaires pour manipuler les graphes, comme la fonction `reconstruct_path` pour reconstruire le chemin le plus court.
*   **`main.py`** :
    *   Contient la fonction `main` qui coordonne l'interaction avec l'utilisateur pour les algorithmes de graphes.
    *  Permet de répéter les processus.
*  **`knapsack_interactive.py`** :
   *  Implémentation interactive de l'algorithme du sac à dos 0/1 en utilisant la programmation dynamique.
   *   Permet à l'utilisateur d'entrer la valeur et le poids des objets et le poids maximal du sac à dos.
* **`merge_intervals_interactive.py`** :
    * Implémentation interactive de la fusion d'intervalles qui se chevauchent.
    * Permet à l'utilisateur de saisir une série d'intervalles et affiche les intervalles fusionnés.
* **`kadane_interactive.py`** :
    * Implémentation interactive de l'algorithme de Kadane pour trouver la somme maximale d'un sous-tableau.
    * Permet à l'utilisateur d'entrer ou de générer un tableau et affiche la somme maximale.
*   **`README.md`** :
    *   Ce fichier, contenant une description du projet et des instructions pour son utilisation.
*   **`report.md`**:
      * Le rapport final, contenant la description des problèmes, des solutions, des résultats et une analyse de la performance.

## Description des Algorithmes

Ce dépôt contient les implémentations des algorithmes suivants :

1.  **Binary Search (Recherche Binaire):** Un algorithme de recherche efficace pour trouver une valeur cible dans une liste triée. Complexité temporelle : O(log n).
2.  **Breadth-First Search (BFS) et Depth-First Search (DFS):** Algorithmes de parcours de graphes. BFS trouve les plus courts chemins dans un graphe non pondéré et DFS permet l'exploration en profondeur et la détection de cycles. Complexité temporelle : O(V + E).
3.  **Knapsack Problem 0/1 (Problème du Sac à Dos 0/1):** Utilise la programmation dynamique pour maximiser la valeur des objets dans un sac à dos, en respectant une limite de poids. Complexité temporelle : O(n * W).
4.  **Merge Intervals (Fusion d'Intervalles):** Un algorithme pour fusionner les intervalles de temps qui se chevauchent. Complexité temporelle : O(n log n).
5.  **Maximum Subarray Sum (Somme Maximale d'un Sous-Tableau):** Implémentation de l'algorithme de Kadane pour trouver la somme maximale d'un sous-tableau contigu. Complexité temporelle : O(n).

## Comment Utiliser Ce Dépôt

1.  **Cloner le Dépôt :**
    ```bash
    git clone https://github.com/<votre_nom_utilisateur>/<nom_du_depot>.git
    ```
2.  **Navigation :** Naviguez dans le répertoire du projet `cd <nom_du_depot>`.
3.  **Exécuter les Codes :**
    *   Pour exécuter l'algorithme de recherche binaire, utilisez :
        ```bash
        python binary_search_interactive.py
        ```
    *  Pour exécuter les algorithmes de parcours de graphe (BFS, DFS), utilisez :
        ```bash
         python main.py
        ```
    *    Pour exécuter l'algorithme du sac à dos, utilisez :
        ```bash
        python knapsack_interactive.py
        ```
    *    Pour exécuter l'algorithme de fusion d'intervalles, utilisez :
        ```bash
        python merge_intervals_interactive.py
         ```
    *    Pour exécuter l'algorithme de Kadane, utilisez :
        ```bash
         python kadane_interactive.py
        ```
4.  **Instructions :** Les programmes vous demanderont les entrées nécessaires à chaque exécution. Suivez les instructions affichées dans la console.
5. **Rapport :** Une version Markdown du rapport se trouve dans `report.md`.

##  Documentation

*  Chaque fichier `.py` contient un code auto documenté avec de bons commentaires.
*   Les fonctions sont documentées avec des docstrings expliquant leurs rôles, leurs arguments et leurs valeurs de retour.
*   Les différents algorithmes sont expliqués dans le rapport `report.md`.
*   Les choix de conception sont aussi expliqués dans le rapport.

## Contribution

Les contributions à ce projet sont les bienvenues. Vous pouvez :

*   Signaler des erreurs ou des améliorations en utilisant les "Issues" de GitHub.
*   Proposer des modifications en créant des "Pull Requests".
*   Partager vos idées et vos suggestions dans les discussions du projet.

## Auteur

*   DONGMO DJOUAKE LEONEL MAKEN 20U2922
