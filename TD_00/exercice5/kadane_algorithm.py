import random

def kadane_algorithm(arr):
    """
    Trouve la somme maximale d'un sous-tableau contigu en utilisant l'algorithme de Kadane.

    Args:
        arr (list): Un tableau d'entiers.

    Returns:
        int: La somme maximale d'un sous-tableau contigu.
    """
    max_so_far = float('-inf')  # Initialisation de la somme maximale vue jusqu'ici
    max_ending_here = 0  # Initialisation de la somme maximale du sous-tableau actuel
    start_index = 0  # Index de début du sous-tableau
    end_index = 0  # Index de fin du sous-tableau
    j=0 # Index utilisé pour le déplacement du sous-tableau

    for i, num in enumerate(arr):
        if max_ending_here + num > num: #Si la somme du sous tableau actuelle est bénéfique, on la garde
            max_ending_here += num #On met à jour la somme du sous tableau actuel
        else : #Si la somme du sous tableau actuelle devient une perte
            max_ending_here = num # On réinitialise à l'élément actuel
            j = i # On reset le point de départ du sous tableau potentiel
        if max_ending_here > max_so_far: # Si la somme du sous tableau actuel est meilleure que la meilleure somme vue jusqu'ici
            max_so_far = max_ending_here # On met à jour la meilleure somme vue jusqu'ici
            start_index = j
            end_index = i # On met à jour les indices de début et de fin

    return max_so_far, start_index, end_index

def get_array_from_user():
    """
    Demande à l'utilisateur de choisir entre une liste aléatoire ou une liste qu'il saisit
    et retourne une liste d'entiers
    """
    while True :
        try:
             choice = input("Voulez-vous saisir votre propre liste d'entiers (s) ou une liste aléatoire (a) ? ").lower()
             if choice == "s": # Choisir de saisir sa propre liste
                   while True :
                       try:
                           input_str = input("Entrez votre liste d'entiers séparés par des espaces : ")
                           numbers = [int(x) for x in input_str.split()]
                           return numbers;
                       except ValueError:
                           print("Veuillez entrer une liste d'entiers valides.")
             elif choice == "a": # Choisir une liste aléatoire
                 while True :
                     try:
                        size = int(input("Entrez la taille de la liste aléatoire : "))
                        if size <= 0:
                             print("Veuillez entrer une taille de liste strictement positive.")
                             continue;
                        lower_bound = int(input("Entrez la borne inférieure de la liste aléatoire : "))
                        upper_bound = int(input("Entrez la borne supérieure de la liste aléatoire : "))
                        if lower_bound >= upper_bound:
                            print("La borne supérieure doit être plus grande que la borne inférieure.")
                            continue;
                        random_numbers = [random.randint(lower_bound, upper_bound) for _ in range(size)]
                        return random_numbers
                     except ValueError:
                         print("Veuillez entrer des entiers valides pour la taille et les bornes.")
             else:
                print("Veuillez choisir entre 's' ou 'a'.")
        except ValueError:
             print("Veuillez entrer une valeur valide")




def main():
    """
    Fonction principale pour interagir avec l'utilisateur, collecter les données du tableau,
    exécuter l'algorithme de Kadane, afficher les résultats et permettre la répétition.
    """
    print("Bienvenue dans le programme de la somme maximale d'un sous-tableau !\n")


    while True: # Boucle pour permettre de faire plusieurs calculs
         arr = get_array_from_user()

         max_sum, start_index, end_index = kadane_algorithm(arr) # Appel de la fonction

         print("\nTableau :", arr)
         print("Somme maximale :", max_sum)
         print("Indices du sous-tableau (début, fin) :", start_index, end_index)

         continue_calculation = input("Voulez-vous calculer la somme maximale d'un autre tableau ? (oui/non) : ").lower()
         if continue_calculation != "oui":
             print("\nAu revoir!")
             break  # Sort de la boucle si l'utilisateur ne veut pas continuer
         print() # New line for readability



if __name__ == "__main__":
    main()