# ===========================================================
# CO5 - Probabilistic Reasoning
# Viral & Infectious Disease Diagnosis Reasoning Engine
# ===========================================================

import random

# -----------------------------------------------------------
# Patient Profile
# -----------------------------------------------------------

prob_patient = {
    "name": "Anita Sharma",
    "age": 29,
    "gender": "Female",
    "symptoms": [
        "high_fever",
        "chills",
        "sweating",
        "nausea",
        "muscle_pain"
    ],
    "travel_history": "Returned from Rajasthan 7 days ago"
}

# -----------------------------------------------------------
# Disease Prior Probabilities
# -----------------------------------------------------------

disease_priors = {
    "Dengue":      0.25,
    "Malaria":     0.40,
    "Typhoid":     0.20,
    "COVID-19":    0.10,
    "Chikungunya": 0.05
}

# -----------------------------------------------------------
# Likelihood P(Symptoms | Disease)
# -----------------------------------------------------------

likelihoods = {
    "Dengue":      0.65,
    "Malaria":     0.88,
    "Typhoid":     0.55,
    "COVID-19":    0.30,
    "Chikungunya": 0.45
}

# -----------------------------------------------------------
# Evidence P(Symptoms)
# -----------------------------------------------------------

evidence_prob = 0.50

# -----------------------------------------------------------
# Bayesian Network
# -----------------------------------------------------------

bayesian_network = {
    "Dengue": [
        "high_fever", "severe_headache",
        "joint_pain", "skin_rash", "bleeding_gums"
    ],
    "Malaria": [
        "chills", "high_fever",
        "sweating", "nausea", "muscle_pain"
    ],
    "Typhoid": [
        "prolonged_fever", "abdominal_pain",
        "weakness", "loss_of_appetite"
    ],
    "COVID-19": [
        "dry_cough", "high_fever",
        "loss_of_smell", "breathlessness"
    ],
    "Chikungunya": [
        "joint_pain", "skin_rash",
        "high_fever", "swollen_joints"
    ]
}

# -----------------------------------------------------------
# Bayes Theorem
# -----------------------------------------------------------

def bayes_theorem(prior, likelihood, evidence):

    return (likelihood * prior) / evidence

# -----------------------------------------------------------
# Bayesian Inference
# -----------------------------------------------------------

def bayesian_inference():

    print("\nBayesian Inference Results:\n")

    results = {}

    for disease in disease_priors:

        posterior = bayes_theorem(
            disease_priors[disease],
            likelihoods[disease],
            evidence_prob
        )

        results[disease] = posterior

        print(f"  {disease} -> Posterior = {posterior:.4f}")

    best = max(results, key=results.get)
    print(f"\n  Most Probable Disease: {best}")

    return results

# -----------------------------------------------------------
# Variable Elimination
# -----------------------------------------------------------

def variable_elimination():

    print("\nVariable Elimination:\n")

    hidden = "viral_load"

    print(f"  Eliminating hidden variable: {hidden}")

    combined = sum(
        disease_priors[d] * likelihoods[d]
        for d in disease_priors
    )

    print(f"  Combined Marginal Probability = {combined:.4f}")

# -----------------------------------------------------------
# Belief Propagation
# -----------------------------------------------------------

def belief_propagation():

    print("\nBelief Propagation:\n")

    for disease, syms in bayesian_network.items():

        matched = sum(
            1 for s in syms
            if s in prob_patient["symptoms"]
        )

        belief = matched / len(syms)

        print(f"  {disease} -> Belief Score = {belief:.2f}")

# -----------------------------------------------------------
# Rejection Sampling
# -----------------------------------------------------------

def rejection_sampling(samples=1000):

    print("\nRejection Sampling:\n")

    accepted = sum(
        1 for _ in range(samples)
        if random.random() < 0.45
    )

    print(f"  Estimated Probability = {accepted / samples:.4f}")

# -----------------------------------------------------------
# Likelihood Weighting
# -----------------------------------------------------------

def likelihood_weighting(samples=1000):

    print("\nLikelihood Weighting:\n")

    weights = [random.uniform(0.4, 1.0) for _ in range(samples)]

    estimate = sum(weights) / len(weights)

    print(f"  Weighted Estimate = {estimate:.4f}")

# -----------------------------------------------------------
# Markov Chain
# -----------------------------------------------------------

def markov_chain(steps=6):

    print("\nMarkov Chain Simulation:\n")

    states = ["Healthy", "Exposed", "Infected", "Recovering"]

    current = "Healthy"

    for step in range(steps):

        print(f"  Step {step + 1}: {current}")

        if current == "Healthy":
            current = random.choice(["Healthy", "Exposed"])

        elif current == "Exposed":
            current = random.choice(["Exposed", "Infected"])

        elif current == "Infected":
            current = random.choice(["Infected", "Recovering"])

        else:
            current = random.choice(["Recovering", "Healthy"])

# -----------------------------------------------------------
# HMM Tracking
# -----------------------------------------------------------

def hmm_tracking():

    print("\nHidden Markov Model Tracking:\n")

    hidden_states  = ["Asymptomatic", "Pre-symptomatic", "Symptomatic"]
    observations   = ["Normal Temp", "Mild Fever", "High Fever", "Chills"]

    for i in range(5):

        hidden   = random.choice(hidden_states)
        observed = random.choice(observations)

        print(f"  Hidden State: {hidden:<20} | "
              f"Observation: {observed}")

# -----------------------------------------------------------
# Sensor Fusion
# -----------------------------------------------------------

def sensor_fusion():

    print("\nSensor Fusion (Multi-Vital Analysis):\n")

    temperature  = 103.4
    platelet_count = 85000
    wbc_count    = 3200

    print(f"  Temperature    : {temperature} F")
    print(f"  Platelet Count : {platelet_count}")
    print(f"  WBC Count      : {wbc_count}")

    if temperature > 102 and platelet_count < 100000:
        print("\n  Alert: Dengue / Malaria Highly Suspected!")

    elif temperature > 102 and wbc_count < 4000:
        print("\n  Alert: Typhoid / Viral Infection Suspected!")

# -----------------------------------------------------------
# Expected Utility
# -----------------------------------------------------------

def expected_utility():

    print("\nExpected Utility of Treatments:\n")

    treatments = {
        "Artemisinin":   {"p_success": 0.92, "utility": 95},
        "Ciprofloxacin": {"p_success": 0.85, "utility": 80},
        "IV_Fluids":     {"p_success": 0.70, "utility": 65}
    }

    for t, d in treatments.items():

        ev = d["p_success"] * d["utility"]

        print(f"  {t} -> Expected Utility = {ev:.2f}")

# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("\n" + "=" * 50)
print("VIRAL & INFECTIOUS DISEASE DIAGNOSIS ENGINE")
print("CO5 - PROBABILISTIC REASONING")
print("=" * 50)

print(f"\nPatient : {prob_patient['name']}")
print(f"Age     : {prob_patient['age']}")
print(f"Travel  : {prob_patient['travel_history']}")

bayesian_inference()

print("\nBayesian Network Structure:\n")
for d, s in bayesian_network.items():
    print(f"  {d} -> {s}")

variable_elimination()
belief_propagation()
rejection_sampling()
likelihood_weighting()
markov_chain()
hmm_tracking()
sensor_fusion()
expected_utility()

print("\n" + "=" * 50)
print("PROBABILISTIC REASONING COMPLETED")
print("=" * 50)

