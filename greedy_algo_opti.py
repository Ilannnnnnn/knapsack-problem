"""
Autheur :
Ilan Jaffeux-Cheniout <ilan.jaffeux--cheniout@isen-ouest.yncrea.fr>

Tous les commentaires sont rédigés par IA 
"""
import time

objets = [
    ('Pompe', 0.2, 1.5),
    ('Démonte-pneus', 0.1, 1.5),
    ('Gourde', 1.0, 2),
    ('Chambre à air', 0.2, 0.5),
    ('Clé de 15', 0.3, 1),
    ('Multi-tool', 0.2, 1.7),
    ('Pince multiprise', 0.4, 0.8),
    ('Couteau suisse', 0.2, 1.5),
    ('Compresses', 0.1, 0.4),
    ('Désinfectant', 0.2, 0.6),
    ('Veste de pluie', 0.4, 1),
    ('Pantalon de pluie', 0.4, 0.75),
    ('Crème solaire', 0.4, 1.75),
    ('Carte IGN', 0.1, 0.2),
    ('Batterie portable', 0.5, 0.4),
    ('Téléphone mobile', 0.4, 2),
    ('Lampes', 0.3, 1.8),
    ('Arrache Manivelle', 0.4, 0),
    ('Bouchon valve chrome bleu', 0.01, 0.1),
    ('Maillon rapide', 0.05, 1.4),
    ('Barre de céréales', 0.4, 0.8),
    ('Fruits', 0.6, 1.3),
    ('Rustines', 0.05, 1.5)
]

# Masse maximale du sac à dos
masse_max = 3.0


def calculer_utilite_et_masse(objets):
    """
    Calcule l'utilité totale et la masse totale d'une liste d'objets.

    Args:
        objets: Une liste de tuples (nom, poids, utilité) représentant les objets.

    Returns:
        Un tuple contenant :
            - L'utilité totale des objets.
            - La masse totale des objets.
    """
    utilite_totale = sum(objet[2] for objet in objets)
    masse_totale = sum(objet[1] for objet in objets)
    return utilite_totale, masse_totale


def greedy_algo(objets, masse_max):
    """
    Trouve une solution initiale au problème du sac à dos avec un algorithme glouton.

    Args:
        objets: Une liste de tuples (nom, poids, utilité) représentant les objets disponibles.
        masse_max: La capacité maximale du sac à dos (en kilogrammes).

    Returns:
        Un tuple contenant :
            - la liste des objets sélectionnés par l'algorithme glouton,
            - la masse totale des objets sélectionnés,
            - l'utilité totale des objets sélectionnés.
    """
    objets_tries = sorted(objets, key=lambda x: x[2] / x[1], reverse=True)
    masse_totale = 0
    utilite_totale = 0
    objets_selectionnes = []
    for objet in objets_tries:
        if masse_totale + objet[1] <= masse_max:
            objets_selectionnes.append(objet)
            masse_totale += objet[1]
            utilite_totale += objet[2]
    return objets_selectionnes, masse_totale, utilite_totale


def recherche_locale(objets, solution_initiale, masse_max):
    """
    Améliore une solution initiale du problème du sac à dos par recherche locale.

    Args:
        objets: Une liste de tuples (nom, poids, utilité) représentant les objets disponibles.
        solution_initiale: Un tuple contenant la liste des objets sélectionnés initialement, leur masse totale et leur utilité totale.
        masse_max: La capacité maximale du sac à dos (en kilogrammes).

    Returns:
        Un tuple contenant :
            - la liste des objets sélectionnés après amélioration,
            - la masse totale des objets sélectionnés,
            - l'utilité totale des objets sélectionnés.
    """
    objets_selectionnes, _, _ = solution_initiale
    objets_non_selectionnes = [objet for objet in objets if objet not in objets_selectionnes]

    meilleure_solution = objets_selectionnes
    meilleure_utilite, meilleure_masse = calculer_utilite_et_masse(meilleure_solution)

  
    def essayer_amelioration(solution, objets_non_selectionnes):
        """
        Essaie d'améliorer une solution en échangeant un objet sélectionné avec un objet non sélectionné.

        Args:
            solution: La solution actuelle (liste d'objets sélectionnés).
            objets_non_selectionnes: La liste des objets non sélectionnés.

        Returns:
            Un tuple contenant :
                - la meilleure solution trouvée après l'échange (peut être la même que la solution initiale si aucune amélioration n'est possible),
                - l'utilité totale de la meilleure solution,
                - la masse totale de la meilleure solution.
        """
        for i, objet_ajouter in enumerate(objets_non_selectionnes):
            for j, objet_retirer in enumerate(solution):
                nouvelle_solution = solution[:j] + [objet_ajouter] + solution[j+1:]
                nouvelle_utilite, nouvelle_masse = calculer_utilite_et_masse(nouvelle_solution)
                if nouvelle_masse <= masse_max and nouvelle_utilite > meilleure_utilite:
                    return nouvelle_solution, nouvelle_utilite, nouvelle_masse
        return solution, meilleure_utilite, meilleure_masse

    # Effectue des améliorations jusqu'à ce qu'il n'y en ait plus
    amelioration_trouvee = True
    while amelioration_trouvee:
        nouvelle_solution, nouvelle_utilite, nouvelle_masse = essayer_amelioration(meilleure_solution, objets_non_selectionnes)
        if nouvelle_utilite > meilleure_utilite:
            meilleure_solution, meilleure_utilite, meilleure_masse = nouvelle_solution, nouvelle_utilite, nouvelle_masse
        else:
            amelioration_trouvee = False

    return meilleure_solution, meilleure_masse, meilleure_utilite

start_time = time.time()
solution_initiale = greedy_algo(objets, masse_max)
solution_optimisee = recherche_locale(objets, solution_initiale, masse_max)
end_time = time.time()
total_time = end_time - start_time

# Afficher les résultats
print("Objets sélectionnés par l'algorithme hybride:")
for objet in solution_optimisee[0]:
    print(objet)
print("Masse totale:", solution_optimisee[1])
print("Utilité totale:", solution_optimisee[2])
print("Temps d'exécution:", total_time)
