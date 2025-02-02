def knapsack_01(items, max_weight):
    """
    Résout le problème du sac à dos 0/1 en utilisant la programmation dynamique.

    Args:
        items (list): Une liste de tuples (valeur, poids) représentant les objets.
        max_weight (int): Le poids maximal du sac à dos.

    Returns:
        int, list: La valeur maximale atteignable et la liste des indices des objets sélectionnés.
    """

    n = len(items)
    # Initialisation du tableau 2D dp
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    # Remplissage du tableau dp
    for i in range(1, n + 1):
      value, weight = items[i-1] # current item
      for w in range(max_weight + 1):
           if weight <= w: # si le poids de l'objet est inférieur à la limite de poids courante
                dp[i][w] = max(value + dp[i-1][w-weight], dp[i-1][w]) # on choisit le max entre inclure l'objet et ne pas l'inclure
           else: # si le poids de l'objet est supérieur à la limite de poids courante
                dp[i][w] = dp[i-1][w] # On ne peut pas inclure l'objet

    # Reconstruction de la solution optimale
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1): # On parcours la matrice de la fin au début
        if dp[i][w] != dp[i-1][w]: # Si la valeur change on sait qu'on a ajouté l'objet
            selected_items.append(i-1) # On ajoute l'objet à la liste
            w -= items[i-1][1]   # On enlève le poids de l'objet du poids actuel
    return dp[n][max_weight], selected_items # On retourne la valeur max et la liste des indices des objets sélectionnés

def get_items_from_user():
    """
    Demande à l'utilisateur de saisir les informations sur les objets (valeur, poids) et retourne une liste de tuples.
    """
    items = []
    while True:
        try:
            num_items = int(input("Combien d'objets voulez-vous considérer ? "))
            if num_items <= 0:
                 print("Veuillez entrer un nombre d'objets strictement positif.")
                 continue
            for i in range(num_items):
                while True:
                    try:
                        input_str = input(f"Entrez la valeur et le poids de l'objet {i+1}, séparés par un espace (par ex., '100 20'): ")
                        value, weight = map(int, input_str.split())
                        if value < 0 or weight < 0:
                            print("Veuillez entrer une valeur et un poids positif.")
                            continue;
                        items.append((value, weight))
                        break
                    except ValueError:
                        print("Veuillez entrer deux entiers valides.")
            return items;
        except ValueError:
            print("Veuillez entrer un entier valide pour le nombre d'objets.")


def get_max_weight_from_user():
    """
    Demande à l'utilisateur de saisir le poids maximal du sac et le retourne.
    """
    while True :
        try:
            max_weight = int(input("Entrez le poids maximal du sac à dos : "))
            if max_weight <= 0 :
                print("Veuillez entrer un poids maximal strictement positif.")
                continue;
            return max_weight
        except ValueError:
            print("Veuillez entrer un entier valide.")


def main():
    """
    Fonction principale pour interagir avec l'utilisateur, collecter les données des objets,
    du poids du sac, exécuter l'algorithme du sac à dos, afficher les résultats et permettre la répétition.
    """
    print("Bienvenue dans le programme du sac à dos 0/1 !\n")

    while True:  # Boucle pour permettre des résolutions multiples
        items = get_items_from_user()
        max_weight = get_max_weight_from_user()

        max_value, selected_items = knapsack_01(items, max_weight) # Appel de la fonction

        print("\nObjets :", items)
        print("Poids maximum du sac :", max_weight)
        print("Valeur maximale atteignable :", max_value)
        print("Indices des objets sélectionnés (commençant à 0) :", selected_items)

        continue_solving = input("Voulez-vous résoudre un autre problème du sac à dos ? (oui/non) : ").lower()
        if continue_solving != "oui":
            print("Au revoir!")
            break  # Sort de la boucle si l'utilisateur ne veut pas continuer
        print() # New line for readability


if __name__ == "__main__":
    main()