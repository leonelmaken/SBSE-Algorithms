def merge_intervals(intervals):
    """
    Fusionne une liste d'intervalles qui se chevauchent.

    Args:
        intervals (list): Une liste de tuples (start_time, end_time) représentant les intervalles.

    Returns:
        list: Une liste d'intervalles fusionnés (tuples (start_time, end_time)).
    """
    if not intervals:
      return []
    # Tri des intervalles par heure de début
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = [sorted_intervals[0]]
    for start, end in sorted_intervals[1:]:
        last_start, last_end = merged_intervals[-1]

        if start <= last_end:
            merged_intervals[-1] = (last_start, max(end, last_end))
        else:
            merged_intervals.append((start, end))
    return merged_intervals

def get_intervals_from_user():
    """
    Demande à l'utilisateur de saisir les informations sur les intervalles (start_time, end_time) et retourne une liste de tuples.
    """
    intervals = []
    while True:
        try:
            num_intervals = int(input("Combien d'intervalles voulez-vous considérer ? "))
            if num_intervals <= 0:
                print("Veuillez entrer un nombre d'intervalles strictement positif.")
                continue
            for i in range(num_intervals):
                while True:
                    try:
                         input_str = input(f"Entrez le temps de début et le temps de fin de l'intervalle {i+1}, séparés par un espace (par ex., '1 3'): ")
                         start_time, end_time = map(int, input_str.split())
                         if start_time < 0 or end_time < 0:
                            print("Veuillez entrer des temps positifs.")
                            continue
                         if end_time < start_time:
                             print("Le temps de fin doit être supérieur ou égal au temps de début.")
                             continue
                         intervals.append((start_time, end_time))
                         break;
                    except ValueError:
                         print("Veuillez entrer deux entiers valides.")
            return intervals
        except ValueError:
            print("Veuillez entrer un entier valide pour le nombre d'intervalles.")



def main():
    """
    Fonction principale pour interagir avec l'utilisateur, collecter les données des intervalles,
    exécuter l'algorithme de fusion, afficher les résultats et permettre la répétition.
    """
    print("Bienvenue dans le programme de fusion d'intervalles !\n")

    while True:  # Boucle pour permettre des fusions multiples
         intervals = get_intervals_from_user()
         merged_intervals = merge_intervals(intervals) # Appel de la fonction

         print("\nIntervalles originaux :", intervals)
         print("Intervalles fusionnés :", merged_intervals)

         continue_merging = input("Voulez-vous fusionner une autre liste d'intervalles ? (oui/non) : ").lower()
         if continue_merging != "oui":
             print("\nAu revoir!")
             break  # Sort de la boucle si l'utilisateur ne veut pas continuer
         print() # New line for readability

if __name__ == "__main__":
   main()