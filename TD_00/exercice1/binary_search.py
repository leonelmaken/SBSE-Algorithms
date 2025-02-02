def binary_search(sorted_list, target):
    """
    Effectue une recherche binaire dans une liste triée.

    Args:
        sorted_list (list): La liste triée dans laquelle effectuer la recherche.
        target (int): La valeur cible à rechercher.

    Returns:
        int: L'index de la valeur cible si elle est trouvée, -1 sinon (si non trouvée).
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2  # Calcule l'index du milieu
        if sorted_list[mid] == target:
            return mid  # La cible est trouvée, on retourne l'index
        elif sorted_list[mid] < target:
            low = mid + 1  # La cible est plus grande, on cherche dans la moitié droite
        else:
            high = mid - 1  # La cible est plus petite, on cherche dans la moitié gauche
    return -1  # La cible n'est pas dans la liste, on retourne -1


def get_sorted_list_from_user():
    """
    Demande à l'utilisateur de saisir une liste triée d'entiers.

    Returns:
        list: La liste triée saisie par l'utilisateur.
    """
    while True:
        try:
            print("Veuillez entrer une liste d'entiers triés par ordre croissant, séparés par des espaces.")
            print("Exemple : 2 5 8 12 16")  # Exemple pour l'utilisateur
            input_str = input("Votre liste : ")
            numbers = [int(x) for x in input_str.split()]
            if all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1)):
                return numbers # Retourne la liste si elle est bien triée
            else :
                print("La liste n'est pas triée, veuillez la saisir à nouveau.\n")
        except ValueError:
            print("Erreur : Veuillez entrer des entiers valides.\n")
        except IndexError: # catch error if the user enters nothing
            print("Erreur : Veuillez saisir une liste non vide.\n")

def main():
    """
    Fonction principale pour gérer l'interaction avec l'utilisateur.
    """
    print("Bienvenue dans le programme de recherche binaire!\n")
    sorted_list = get_sorted_list_from_user()

    while True:
        try:
            target = int(input("Veuillez entrer l'élément à rechercher dans la liste : "))
            index = binary_search(sorted_list, target)

            if index != -1:
                print(f"L'élément {target} se trouve à la position {index} dans la liste.\n")
            else:
                print(f"L'élément {target} n'a pas été trouvé dans la liste.\n")

            continue_search = input("Voulez-vous effectuer une autre recherche ? (oui/non) : ").lower()
            if continue_search != "oui":
                print("Au revoir!")
                break # Arrête la boucle si l'utilisateur ne souhaite pas continuer
            print() # New line for readability

        except ValueError:
            print("Erreur : Veuillez entrer un entier valide pour la recherche.\n")

if __name__ == "__main__":
    main()