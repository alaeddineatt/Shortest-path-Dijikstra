
  
import re
from time import time
from psutil._compat import xrange


# Script pour l'algorithme de Dijkstra
def dijkstra(graph, startP, targetP):
    inf = 0
    for u in graph:
        for v, w in graph[u]:
            inf = inf + w
    dist = dict([(u, inf) for u in graph]) # Calcul de distance
    prev = dict([(u, None) for u in graph])# Variable précédente
    q = list(graph)
    dist[startP] = 0 # Distance de point de démarrage
    def x(v):
        return dist[v] #retourner la distance actuelle
    while q: # Algo principale dijikstra
        u = min(q, key=x)
        q.remove(u)
        for v, w in graph[u]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    trav = []
    temp = targetP
    while temp != startP: # Calcule de traversée
        trav.append(prev[temp])
        temp = prev[temp]
    trav.reverse()
    trav.append(targetP)
    return trav, dist[targetP] # Retourner comme résultat la traversée et la distance


# Liste vers Graphe pour l'algorithme de Dijikstra
def dijAlgo(lists_sources_lists):
    for k in xrange(len(list_keys)):
        for unit in list_source_destination:
            if unit[0] == k:
                lists_sources_lists.append((unit[1], unit[2]))
            else:
                pass
        if len(lists_sources_lists) != 0:
            graph_dijkstra[k] = lists_sources_lists
            lists_sources_lists = []


# Joindre le chemin le plus court avec le dictionnaire (n° de chaque station)
def short_path(l, dict_stations, flag=None):
    list_station = []
    index = 0
    for unit in l:
        index = index + 1
        list_station.append(("[{0}] Station N°{1}: {2}".format(index, unit, dict_stations[unit])))
    if flag:
        return ''.join(list_station)
    else:
        return list_station


def dictionary():
    # Création de dictionnaire en chargeant le jeu de données (dataset) (.txt)
    for i in xrange(len(line_dataset) - 1):
        # xrange() Génèration des nombres à la demande
        # range() pré-calcule tous les nombres et les enregistre en mémoire, ce qui provoque l'erreur.
        if not re.match(r'([\d]+)', line_dataset[i]):
            line_temp = i

    for i in xrange(line_temp + 1, len(line_dataset) - 1):
        list_source_destination.append(
            (int(line_dataset[i].strip().split(" ")[0]), int(line_dataset[i].strip().split(" ")[1]),
             float(line_dataset[i].strip().split(" ")[2])))
        list_keys.append(int(line_dataset[i].strip().split(" ")[0]))


# dataset avec dictionnaire
def dataset_with_dict():
    # Variable locale pour l'ensemble de données (dataset)
    f = open('metro_paris.txt', 'r') # Ouverture de fichier
    stations_with_dictinary = []
    my_stations_with_dict = {}
    for unit in f.readlines()[1:]:
        if unit.strip() != '[Edges]': #Tant que la ligne représente un nom d'une station
            stations_with_dictinary.append(unit[5:])
        else:
            break
    for i in xrange(len(stations_with_dictinary)):# Convertir la liste en dictionnaire
        my_stations_with_dict[i] = stations_with_dictinary[i]
    return my_stations_with_dict


if __name__ == "__main__":
    # Ouverture de fichier metro_paris.txt + déclaration des structures nécéssaires à l'implémentation
    dataset = open("metro_paris.txt", "r")
    list_source_destination = []
    list_keys = []
    graph_dijkstra = {}
    lists_sources_lists = []
    line_dataset = dataset.readlines()
    dictionary()
    # Déclarer une variable locale pour la fonction dataset_with_dict()
    dict_my_stations = dataset_with_dict()
    dijAlgo(lists_sources_lists)
    print('------------Algorithme de Dijkstra le plus court chemin-------------')
    startPoint = int(input("\nEntrer N° de point de départ (-1 pour afficher la liste des stations disponibles): "))
    if startPoint==-1 :
        print("\nStations disponibles :\n")
        print(short_path(dict_my_stations, dict_my_stations, "p"))
        startPoint = int(input("Entrer N° de point de départ: "))
    targetPoint = int(input("Entrer N° de point d'arrivée: "))
    # Début chronomètre pour calculer le temps d'exécution
    f0 = time()
    # Déclarer une variable locale pour calculer le chemin et sa distance
    traverse = dijkstra(graph_dijkstra, startPoint, targetPoint)[0]
    distance = dijkstra(graph_dijkstra, startPoint, targetPoint)[1]
    # Afficher la traversée de chemin
    print()
    print("Le chemin le plus court entre", startPoint, "et", targetPoint, " est:\n", traverse, "\n")
    # Afficher les stations parcourues dans le chemin en utilisant le dictionnaire des stations
    print("Stations parcourues :\n")
    print(short_path(traverse, dict_my_stations, "p"))
    # Afficher la distance parcourue
    print("Distance parcourue:",
          ("%.0f" % distance), '\n')
    # Temps d'exécution : Arret de chronomètre
    f1 = time()
    print("Temps d'exécution d'algorithme : %f" % (f1 - f0), "secondes")