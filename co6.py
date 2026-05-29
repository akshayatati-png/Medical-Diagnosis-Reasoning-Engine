# ===========================================================
# CO6 - Hybrid AI System
# Viral & Infectious Disease Diagnosis Reasoning Engine
# ===========================================================

import heapq
import random

# -----------------------------------------------------------
# Patient Profile
# -----------------------------------------------------------

hybrid_patient = {
    "name":     "Priya Nair",
    "age":      31,
    "gender":   "Female",
    "symptoms": [
        "high_fever",
        "dry_cough",
        "loss_of_smell",
        "fatigue",
        "breathlessness"
    ],
    "allergies": ["chloroquine", "ibuprofen"],
    "travel_history": "Returned from Delhi 4 days ago",
    "severity": 7
}

# -----------------------------------------------------------
# Integrated Disease Database
# -----------------------------------------------------------

hybrid_diseases = {

    "Dengue": {
        "symptoms":     ["high_fever", "severe_headache", "joint_pain", "skin_rash"],
        "probability":  0.55,
        "treatments":   ["Paracetamol", "IV_Fluids", "Aspirin"],
        "cost":         3
    },

    "Malaria": {
        "symptoms":     ["chills", "high_fever", "sweating", "nausea", "muscle_pain"],
        "probability":  0.45,
        "treatments":   ["Chloroquine", "Artemisinin", "Primaquine"],
        "cost":         2
    },

    "Typhoid": {
        "symptoms":     ["prolonged_fever", "abdominal_pain", "weakness", "loss_of_appetite"],
        "probability":  0.35,
        "treatments":   ["Ciprofloxacin", "Azithromycin", "Ceftriaxone"],
        "cost":         4
    },

    "COVID-19": {
        "symptoms":     ["dry_cough", "high_fever", "loss_of_smell", "breathlessness", "fatigue"],
        "probability":  0.90,
        "treatments":   ["Remdesivir", "Dexamethasone", "Oxygen_Support"],
        "cost":         1
    },

    "Chikungunya": {
        "symptoms":     ["joint_pain", "skin_rash", "high_fever", "swollen_joints"],
        "probability":  0.30,
        "treatments":   ["Ibuprofen", "Naproxen", "Rest_Therapy"],
        "cost":         3
    }
}

# -----------------------------------------------------------
# Explainability Logs
# -----------------------------------------------------------

hybrid_logs = []

# -----------------------------------------------------------
# CO2 - Heuristic Function
# -----------------------------------------------------------

def hybrid_heuristic(patient_symptoms, disease_symptoms):

    return sum(
        1 for s in disease_symptoms
        if s not in patient_symptoms
    )

# -----------------------------------------------------------
# CO2 - A* Search
# -----------------------------------------------------------

def hybrid_a_star():

    print("\nA* SEARCH (CO2):\n")

    pq = []

    for disease, info in hybrid_diseases.items():

        g = info["cost"]
        h = hybrid_heuristic(hybrid_patient["symptoms"], info["symptoms"])
        f = g + h

        heapq.heappush(pq, (f, disease))

    ranked = []

    while pq:

        score, disease = heapq.heappop(pq)

        print(f"  {disease} -> f(n) = {score}")

        ranked.append(disease)

    return ranked

# -----------------------------------------------------------
# CO3 - Constraint Check
# -----------------------------------------------------------

def is_safe_treatment(treatment):

    for allergy in hybrid_patient["allergies"]:

        if treatment.lower() == allergy.lower():

            hybrid_logs.append(
                f"[REJECTED] {treatment} — Allergy to {allergy}"
            )

            return False

    return True

# -----------------------------------------------------------
# CO3 - Forward Checking
# -----------------------------------------------------------

def hybrid_forward_checking():

    print("\nFORWARD CHECKING (CO3):\n")

    valid = {}

    for disease, info in hybrid_diseases.items():

        safe_treatments = [
            t for t in info["treatments"]
            if is_safe_treatment(t)
        ]

        valid[disease] = safe_treatments

        print(f"  {disease} -> {safe_treatments}")

    return valid

# -----------------------------------------------------------
# CO5 - Bayesian Reasoning
# -----------------------------------------------------------

def hybrid_bayesian():

    print("\nBAYESIAN REASONING (CO5):\n")

    probs = {}

    for disease, info in hybrid_diseases.items():

        prior      = info["probability"]
        total      = len(info["symptoms"])
        matched    = sum(
            1 for s in info["symptoms"]
            if s in hybrid_patient["symptoms"]
        )
        likelihood = matched / total if total > 0 else 0
        posterior  = prior * likelihood

        probs[disease] = posterior

        print(f"  {disease} -> Posterior = {posterior:.4f}")

    return probs

# -----------------------------------------------------------
# CO4 - Utility Function
# -----------------------------------------------------------

def hybrid_utility(probability, treatment_count, severity):

    return round(
        (probability * 100)
        - (treatment_count * 4)
        + (severity * 0.5),
        2
    )

# -----------------------------------------------------------
# CO4 - Best Decision
# -----------------------------------------------------------

def hybrid_decision(probabilities, treatments):

    print("\nDECISION MAKING (CO4):\n")

    best_disease = None
    best_utility = -999

    for disease in probabilities:

        utility = hybrid_utility(
            probabilities[disease],
            len(treatments[disease]),
            hybrid_patient["severity"]
        )

        print(f"  {disease} -> Utility = {utility}")

        if utility > best_utility:

            best_utility = utility
            best_disease = disease

    return best_disease

# -----------------------------------------------------------
# CO6 - Explainability
# -----------------------------------------------------------

def hybrid_explain(final_disease, safe_treatments):

    print("\nEXPLAINABILITY (CO6):\n")

    print(f"  Patient       : {hybrid_patient['name']}")
    print(f"  Age / Gender  : {hybrid_patient['age']} / {hybrid_patient['gender']}")
    print(f"  Travel History: {hybrid_patient['travel_history']}")

    print(f"\n  Predicted Disease: {final_disease}")

    print("\n  Matched Symptoms:")

    for s in hybrid_diseases[final_disease]["symptoms"]:

        if s in hybrid_patient["symptoms"]:
            print(f"    [+] {s}")

    print(f"\n  Recommended Treatments: {safe_treatments[final_disease]}")

    print("\n  Constraint & Decision Logs:")

    for log in hybrid_logs:
        print(f"    {log}")

# -----------------------------------------------------------
# Failure Analysis
# -----------------------------------------------------------

def failure_analysis():

    print("\nFAILURE ANALYSIS:\n")

    issues = [
        "Limited to 5 viral diseases — rare diseases not covered",
        "Probabilities are manually assigned, not learned from data",
        "No real-time lab reports integrated",
        "Travel history used qualitatively, not quantitatively"
    ]

    for issue in issues:
        print(f"  - {issue}")

# -----------------------------------------------------------
# Ethics & Limitations
# -----------------------------------------------------------

def ethics_limitations():

    print("\nETHICS & LIMITATIONS:\n")

    points = [
        "AI diagnosis must be validated by a certified physician",
        "Bias may exist due to limited symptom dataset",
        "Not suitable for pediatric or geriatric patients without tuning",
        "Privacy of patient data must be strictly maintained"
    ]

    for point in points:
        print(f"  - {point}")

# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("\n" + "=" * 50)
print("VIRAL & INFECTIOUS DISEASE DIAGNOSIS ENGINE")
print("CO6 - HYBRID AI SYSTEM")
print("=" * 50)

# CO2 - Search
search_ranked = hybrid_a_star()

# CO3 - CSP
safe_treatments = hybrid_forward_checking()

# CO5 - Probability
prob_results = hybrid_bayesian()

# CO4 - Decision
final = hybrid_decision(prob_results, safe_treatments)

print(f"\nFINAL DIAGNOSIS: {final}")

# CO6 - Explain
hybrid_explain(final, safe_treatments)

# Performance
print("\nPERFORMANCE SUMMARY:\n")
print(f"  Symptoms Analyzed : {len(hybrid_patient['symptoms'])}")
print(f"  Diseases Evaluated: {len(hybrid_diseases)}")
print(f"  Severity Level    : {hybrid_patient['severity']}/10")

# Failure Analysis
failure_analysis()

# Ethics
ethics_limitations()

print("\n" + "=" * 50)
print("HYBRID AI PROCESS COMPLETED")
print("=" * 50)
