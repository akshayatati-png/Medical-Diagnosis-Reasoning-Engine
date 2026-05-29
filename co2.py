# ===========================================================
# CO2 - Search Algorithms
# Viral & Infectious Disease Diagnosis Reasoning Engine
# ===========================================================

from collections import deque
import heapq
import time

# -----------------------------------------------------------
# Disease Database with Costs
# -----------------------------------------------------------

VIRAL_DISEASE_DB = {

    "Dengue": {
        "symptoms": [
            "high_fever",
            "severe_headache",
            "joint_pain",
            "skin_rash",
            "bleeding_gums"
        ],
        "cost": 3
    },

    "Malaria": {
        "symptoms": [
            "chills",
            "high_fever",
            "sweating",
            "nausea",
            "muscle_pain"
        ],
        "cost": 2
    },

    "Typhoid": {
        "symptoms": [
            "prolonged_fever",
            "abdominal_pain",
            "weakness",
            "loss_of_appetite",
            "constipation"
        ],
        "cost": 4
    },

    "COVID-19": {
        "symptoms": [
            "dry_cough",
            "high_fever",
            "loss_of_smell",
            "breathlessness",
            "fatigue"
        ],
        "cost": 1
    },

    "Chikungunya": {
        "symptoms": [
            "joint_pain",
            "skin_rash",
            "high_fever",
            "swollen_joints"
        ],
        "cost": 3
    }
}

# -----------------------------------------------------------
# Patient Symptoms for Search
# -----------------------------------------------------------

SEARCH_PATIENT_SYMPTOMS = [
    "high_fever",
    "joint_pain",
    "skin_rash"
]

# -----------------------------------------------------------
# Heuristic Function
# h(n) = Number of unmatched symptoms
# -----------------------------------------------------------

def heuristic_unmatched(patient_symptoms, disease_symptoms):

    unmatched = 0

    for symptom in disease_symptoms:

        if symptom not in patient_symptoms:
            unmatched += 1

    return unmatched

# -----------------------------------------------------------
# BFS Search
# -----------------------------------------------------------

def bfs_search():

    print("\n" + "=" * 40)
    print("BREADTH FIRST SEARCH (BFS)")
    print("=" * 40)

    start_time = time.time()

    queue = deque(VIRAL_DISEASE_DB.keys())
    visited = set()
    node_expansions = 0

    while queue:

        disease = queue.popleft()

        if disease not in visited:

            visited.add(disease)
            node_expansions += 1

            matched = [
                s for s in VIRAL_DISEASE_DB[disease]["symptoms"]
                if s in SEARCH_PATIENT_SYMPTOMS
            ]

            print(f"Visited: {disease} | Matched Symptoms: {matched}")

    end_time = time.time()

    print(f"\nTotal Node Expansions: {node_expansions}")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# -----------------------------------------------------------
# DFS Search
# -----------------------------------------------------------

def dfs_recursive(diseases, visited, node_expansions):

    if not diseases:
        return node_expansions

    disease = diseases.pop()

    if disease not in visited:

        visited.add(disease)
        node_expansions += 1

        matched = [
            s for s in VIRAL_DISEASE_DB[disease]["symptoms"]
            if s in SEARCH_PATIENT_SYMPTOMS
        ]

        print(f"Visited: {disease} | Matched Symptoms: {matched}")

    return dfs_recursive(diseases, visited, node_expansions)


def dfs_search():

    print("\n" + "=" * 40)
    print("DEPTH FIRST SEARCH (DFS)")
    print("=" * 40)

    start_time = time.time()

    diseases = list(VIRAL_DISEASE_DB.keys())
    visited = set()

    node_expansions = dfs_recursive(diseases, visited, 0)

    end_time = time.time()

    print(f"\nTotal Node Expansions: {node_expansions}")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# -----------------------------------------------------------
# Uniform Cost Search (UCS)
# -----------------------------------------------------------

def ucs_search():

    print("\n" + "=" * 40)
    print("UNIFORM COST SEARCH (UCS)")
    print("=" * 40)

    start_time = time.time()

    priority_queue = []
    visited = set()
    node_expansions = 0

    for disease, info in VIRAL_DISEASE_DB.items():
        heapq.heappush(priority_queue, (info["cost"], disease))

    while priority_queue:

        cost, disease = heapq.heappop(priority_queue)

        if disease not in visited:

            visited.add(disease)
            node_expansions += 1

            print(f"Visited: {disease} | Cost: {cost}")

    end_time = time.time()

    print(f"\nTotal Node Expansions: {node_expansions}")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# -----------------------------------------------------------
# Greedy Best First Search
# -----------------------------------------------------------

def greedy_search():

    print("\n" + "=" * 40)
    print("GREEDY BEST FIRST SEARCH")
    print("=" * 40)

    start_time = time.time()

    priority_queue = []
    visited = set()
    node_expansions = 0

    for disease, info in VIRAL_DISEASE_DB.items():

        h = heuristic_unmatched(
            SEARCH_PATIENT_SYMPTOMS,
            info["symptoms"]
        )

        heapq.heappush(priority_queue, (h, disease))

    while priority_queue:

        h, disease = heapq.heappop(priority_queue)

        if disease not in visited:

            visited.add(disease)
            node_expansions += 1

            print(f"Visited: {disease} | Heuristic h(n): {h}")

    end_time = time.time()

    print(f"\nTotal Node Expansions: {node_expansions}")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# -----------------------------------------------------------
# A* Search
# -----------------------------------------------------------

def a_star_search():

    print("\n" + "=" * 40)
    print("A* SEARCH ALGORITHM")
    print("=" * 40)

    start_time = time.time()

    open_set = []
    closed_set = set()
    node_expansions = 0
    tie_breaker = 0

    for disease, info in VIRAL_DISEASE_DB.items():

        g = info["cost"]

        h = heuristic_unmatched(
            SEARCH_PATIENT_SYMPTOMS,
            info["symptoms"]
        )

        f = g + h

        heapq.heappush(open_set, (f, tie_breaker, disease))
        tie_breaker += 1

    while open_set:

        f, _, disease = heapq.heappop(open_set)

        if disease not in closed_set:

            closed_set.add(disease)
            node_expansions += 1

            print(f"Visited: {disease} | f(n) = g + h = {f}")

    end_time = time.time()

    print(f"\nTotal Node Expansions: {node_expansions}")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("\n" + "=" * 50)
print("VIRAL & INFECTIOUS DISEASE DIAGNOSIS ENGINE")
print("CO2 - SEARCH ALGORITHMS")
print("=" * 50)

print(f"\nPatient Symptoms: {SEARCH_PATIENT_SYMPTOMS}")

bfs_search()
dfs_search()
ucs_search()
greedy_search()
a_star_search()

print("\n" + "=" * 50)
print("SEARCH COMPLETED")
print("=" * 50)
