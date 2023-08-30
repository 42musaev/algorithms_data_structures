from typing import Dict, Set

tree_stations = {
    'one_s': {'id', 'nv', 'ut'},
    'two_s': {'wa', 'id', 'mt'},
    'three_s': {'or', 'nv', 'ca'},
    'four_s': {'nv', 'ut'},
    'five_s': {'ca', 'az'},
}


def greedy_algorithm(stations: Dict) -> Set:
    stations_needed = {element for subset in stations.values() for element in subset}
    final_stations = set()

    while stations_needed:
        best_station = None
        covered_station = set()
        for station, states in stations.items():
            covered = states & stations_needed
            if len(covered) > len(covered_station):
                best_station = station
                covered_station = covered
        stations_needed -= covered_station
        final_stations.add(best_station)

    return final_stations


r = greedy_algorithm(tree_stations)
print(r)
