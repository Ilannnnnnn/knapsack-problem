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
masse_max = 0.6

#On cherche le maximum local
def greedy_algo(objets, masse_max):
    """
    Résout le problème du sac à dos en utilisant un algorithme glouton.

    Args:
        objets: Une liste de tuples (nom, poids, utilité) représentant les objets disponibles.
        masse_max: La capacité maximale du sac à dos (en kilogrammes).

    Returns:
        Un tuple contenant :
            - la liste des objets sélectionnés pour maximiser l'utilité,
            - la masse totale des objets sélectionnés,
            - l'utilité totale des objets sélectionnés.
    """
    objets_tries = sorted(objets, key=lambda x: x[2] / x[1], reverse=True)
    masse_totale = 0
    utilite_totale = 0
    objets_selectionnes = []
    # Parcourir les objets triés
    for objet in objets_tries:
        if masse_totale + objet[1] <= masse_max:
            objets_selectionnes.append(objet)
            masse_totale += objet[1]
            utilite_totale += objet[2]
    worst_object = min(objets_selectionnes, key=lambda x: x[2] / x[1])
        
    return objets_selectionnes, masse_totale, utilite_totale

start_time = round(time.time(), 6)
objets_selectionnes, masse_totale, utilite_totale = greedy_algo(objets, masse_max)
end_time = round(time.time(), 6)
total_time = end_time - start_time


# Afficher les résultats
print("Objets sélectionnés par l'algorithme glouton:")
for objet in objets_selectionnes:
    print(objet)
print("Masse totale:", masse_totale)
print("Utilité totale:", utilite_totale)
print("Temps d'exécution:", total_time)