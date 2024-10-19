import time  # Importation du module time pour mesurer le temps d'exécution


# Fonction principale de programmation dynamique pour résoudre le problème du sac à dos
def prog_dynamique(masse_max, masses, utilites, n):
    """
    Résout le problème du sac à dos avec une masse maximale et des objets de différentes masses et utilités.


    Entrées:
    - masse_max: Masse maximale du sac à dos
    - masses: Liste des masses des objets
    - utilites: Liste des utilités des objets
    - n: Nombre d'objets


    Sorties:
    - utilite_maximale: Utilité maximale atteignable
    - objets_selectionnes: Liste des objets sélectionnés
    """


    # Création du tableau 2D pour stocker l'utilité maximale à chaque combinaison d'objets et masses
    tableau = [[0 for _ in range(masse_max + 1)] for _ in range(n + 1)]


    # Boucle pour remplir le tableau 2D
    for i in range(n + 1):
        for m in range(masse_max + 1):
            if i == 0 or m == 0:
                tableau[i][m] = 0  # Utilité est 0 si aucun objet ou masse est 0
            elif masses[i-1] <= m:
                # Si l'objet peut être inclus, on prend le maximum entre l'inclusion de l'objet et son exclusion
                tableau[i][m] = max(utilites[i-1] + tableau[i-1][m-masses[i-1]], tableau[i-1][m])
            else:
                tableau[i][m] = tableau[i-1][m]  # Si l'objet ne peut pas être inclus, on l'exclut


    # Initialisation pour retrouver les objets sélectionnés
    utilite_maximale = tableau[n][masse_max]
    m = masse_max
    objets_selectionnes = []


    # Boucle pour retrouver les objets sélectionnés
    for i in range(n, 0, -1): # Parcours le tableau dans le sens inverse 
        if utilite_maximale <= 0:
            break  # Arrêter si l'utilité maximale est atteinte
        if utilite_maximale == tableau[i-1][m]:
            continue  # Si l'objet n'a pas été inclus, continuer
        else:
            objets_selectionnes.append(objets[i-1])  # Ajouter l'objet sélectionné à la liste
            utilite_maximale -= utilites[i-1]  # Soustraire l'utilité de l'objet sélectionné
            m -= masses[i-1]  # Réduire la masse restante


    return tableau[n][masse_max], objets_selectionnes  # Retourne l'utilité maximale et les objets sélectionnés


# Liste des objets avec leurs poids et utilités
objets = [
    ("Rustines", 0.05, 1.5), ("Maillon rapide", 0.05, 1.4), ("Démonte-pneus", 0.1, 1.5), ("Bouchon valve chrome bleu", 0.01, 0.1),("Multi-tool", 0.2, 1.7),
    ("Pompe", 0.2, 1.5),("Couteau suisse", 0.2, 1.5), ("Lampes", 0.3, 1.8),("Téléphone mobile", 0.4, 2),("Crème solaire", 0.4, 1.75),("Compresses", 0.1, 0.4),
    ("Clé de 15", 0.3, 1),("Désinfectant", 0.2, 0.6),("Chambre à air", 0.2, 0.5),("Veste de pluie", 0.4, 1),("Fruits", 0.6, 1.3), ("Gourde", 1, 2),
    ("Pince multiprise", 0.4, 0.8),("Carte IGN", 0.1, 0.2),("Barre de céréales", 0.4, 0.8),("Pantalon de pluie", 0.4, 0.75),("Batterie portable", 0.5, 0.4),
    ("Arrache Manivelle", 0.4, 0)
]


# Convertir les masses en entiers pour éviter les problèmes de flottants
c = 0.6  # Capacité maximale du sac à dos en unités de masse
masses = [int(objet[1] * 100) for objet in objets]  # Conversion des masses en entiers (exprimés en centi-unités)
utilites = [objet[2] for objet in objets]  # Liste des utilités des objets
n = len(objets)  # Nombre d'objets
masse_max = int(c * 100)  # Conversion de la masse maximale en entier (exprimée en centi-unités)


# Calculer le temps d'exécution
debut_temps = round(time.time(), 6)  # Temps de début de l'exécution
utilite_maximale, objets_selectionnes = prog_dynamique(masse_max, masses, utilites, n)  # Appel de la fonction principale
fin_temps = round(time.time(), 6)  # Temps de fin de l'exécution
temps_total = fin_temps - debut_temps  # Calcul du temps total d'exécution


# Afficher les résultats
print("L'utilité maximale est de :", utilite_maximale)
print("Objets sélectionnés par l'algorithme de programmation dynamique :")
for objet in objets_selectionnes:
    print(objet)
print("Le temps d'exécution est de :", temps_total)