# ===========================================================
# CO4 - Decision Making & Game Reasoning
# Viral & Infectious Disease Diagnosis Reasoning Engine
# ===========================================================

import math
import random

# -----------------------------------------------------------
# Patient Profile
# -----------------------------------------------------------

decision_patient = {
    "name": "Mohammed Ali",
    "age": 45,
    "gender": "Male",
    "symptoms": ["high_fever", "chills", "muscle_pain", "sweating"],
    "severity": 8,
    "medical_history": "Hypertension"
}

# -----------------------------------------------------------
# Treatment Options Database
# success_rate  = benefit (%)
# side_effect   = risk (%)
# cost          = treatment cost (units)
# -----------------------------------------------------------

treatment_options = {

    "Artemisinin": {
        "success_rate":   92,
        "side_effect":    8,
        "cost":           60
    },

    "Chloroquine": {
        "success_rate":   75,
        "side_effect":    15,
        "cost":           25
    },

    "IV_Fluids": {
        "success_rate":   70,
        "side_effect":    5,
        "cost":           40
    },

    "Ciprofloxacin": {
        "success_rate":   85,
        "side_effect":    12,
        "cost":           50
    }
}

# -----------------------------------------------------------
# Utility Function
# Utility = Success - SideEffect - (Cost * Factor)
# -----------------------------------------------------------

def compute_utility(success_rate, side_effect, cost):

    utility = (
        success_rate
        - side_effect
        - (cost * 0.25)
    )

    return round(utility, 2)

# -----------------------------------------------------------
# Evaluate Treatment
# -----------------------------------------------------------

def evaluate(treatment_name):

    data = treatment_options[treatment_name]

    return compute_utility(
        data["success_rate"],
        data["side_effect"],
        data["cost"]
    )

# -----------------------------------------------------------
# Minimax
# -----------------------------------------------------------

def minimax(depth, is_maximizing, treatment_list):

    if depth == 0 or not treatment_list:
        return 0

    if is_maximizing:

        best = -math.inf

        for t in treatment_list:
            val = evaluate(t) + minimax(depth - 1, False, [])
            best = max(best, val)

        return best

    else:

        worst = math.inf

        for t in treatment_list:
            val = evaluate(t) - minimax(depth - 1, True, [])
            worst = min(worst, val)

        return worst

# -----------------------------------------------------------
# Alpha-Beta Pruning
# -----------------------------------------------------------

def alpha_beta(depth, alpha, beta, is_maximizing, treatment_list):

    if depth == 0 or not treatment_list:
        return 0

    if is_maximizing:

        value = -math.inf

        for t in treatment_list:

            score = evaluate(t)
            value = max(value, score)
            alpha = max(alpha, value)

            if beta <= alpha:
                break

        return value

    else:

        value = math.inf

        for t in treatment_list:

            score = evaluate(t)
            value = min(value, score)
            beta  = min(beta, value)

            if beta <= alpha:
                break

        return value

# -----------------------------------------------------------
# Best Policy Selection
# -----------------------------------------------------------

def select_best_policy():

    best_treatment = None
    best_score     = -math.inf

    print("\nUtility Scores:\n")

    for t in treatment_options:

        score = evaluate(t)

        print(f"  {t} -> Utility = {score}")

        if score > best_score:

            best_score     = score
            best_treatment = t

    return best_treatment, best_score

# -----------------------------------------------------------
# Iterative Deepening
# -----------------------------------------------------------

def iterative_deepening(max_depth):

    print("\nIterative Deepening Search:\n")

    for depth in range(1, max_depth + 1):

        score = minimax(depth, True, list(treatment_options.keys()))

        print(f"  Depth {depth} -> Best Score: {score}")

# -----------------------------------------------------------
# Expectimax
# -----------------------------------------------------------

def expectimax():

    print("\nExpectimax Results:\n")

    for t, data in treatment_options.items():

        p_success = data["success_rate"] / 100
        p_fail    = 1 - p_success

        exp_utility = (
            p_success * 100
            - p_fail * data["side_effect"]
        )

        print(f"  {t} -> Expected Utility = {exp_utility:.2f}")

# -----------------------------------------------------------
# Bounded Rationality
# -----------------------------------------------------------

def bounded_rationality():

    return random.choice(list(treatment_options.keys()))

# -----------------------------------------------------------
# Multi-Agent Reasoning
# -----------------------------------------------------------

def multi_agent_reasoning():

    print("\nMulti-Agent Reasoning:\n")

    doctor_choice  = "Artemisinin"
    patient_choice = "Chloroquine"
    lab_agent      = "Ciprofloxacin"

    print(f"  Doctor Agent   : {doctor_choice}")
    print(f"  Patient Agent  : {patient_choice}")
    print(f"  Lab Agent      : {lab_agent}")

    # Doctor's recommendation is final
    print(f"\n  Final Decision : {doctor_choice}")

    return doctor_choice

# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("\n" + "=" * 50)
print("VIRAL & INFECTIOUS DISEASE DIAGNOSIS ENGINE")
print("CO4 - DECISION MAKING MODULE")
print("=" * 50)

print(f"\nPatient : {decision_patient['name']}")
print(f"Age     : {decision_patient['age']}")
print(f"Gender  : {decision_patient['gender']}")
print(f"Severity: {decision_patient['severity']}/10")

# Policy Selection
best_t, best_s = select_best_policy()
print(f"\nSelected Treatment : {best_t}")
print(f"Best Utility Score : {best_s}")

# Minimax
mm_score = minimax(2, True, list(treatment_options.keys()))
print(f"\nMinimax Score = {mm_score}")

# Alpha-Beta
ab_score = alpha_beta(2, -math.inf, math.inf, True, list(treatment_options.keys()))
print(f"Alpha-Beta Score = {ab_score}")

# Iterative Deepening
iterative_deepening(3)

# Expectimax
expectimax()

# Bounded Rationality
quick = bounded_rationality()
print(f"\nBounded Rationality Quick Pick: {quick}")

# Multi-Agent
final = multi_agent_reasoning()

print("\n" + "=" * 50)
print("DECISION PROCESS COMPLETED")
print("=" * 50)
