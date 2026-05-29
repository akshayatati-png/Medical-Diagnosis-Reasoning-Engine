# ===========================================================
# CO3 - Constraint Satisfaction Problem (CSP)
# Viral & Infectious Disease Diagnosis Reasoning Engine
# ===========================================================

# ===========================================================
# CO3 - Constraint Satisfaction Problem (CSP)
# Viral & Infectious Disease Diagnosis Reasoning Engine
# ===========================================================

import random

# -----------------------------------------------------------
# Patient Profile
# -----------------------------------------------------------

csp_patient = {
    "name": "Sneha Reddy",
    "age": 34,
    "gender": "Female",
    "symptoms": ["high_fever", "chills", "nausea", "sweating"],
    "allergies": ["chloroquine", "aspirin"],
    "medical_history": "No prior chronic illness"
}

# -----------------------------------------------------------
# Disease Variables and Treatment Domains
# -----------------------------------------------------------

treatment_variables = {
    "Dengue":     ["Paracetamol", "IV_Fluids", "Aspirin"],
    "Malaria":    ["Chloroquine", "Artemisinin", "Primaquine"],
    "Typhoid":    ["Ciprofloxacin", "Azithromycin", "Ceftriaxone"],
    "COVID-19":   ["Remdesivir", "Dexamethasone", "Oxygen_Support"],
    "Chikungunya":["Ibuprofen", "Naproxen", "Rest_Therapy"]
}

# -----------------------------------------------------------
# Explainability Logs
# -----------------------------------------------------------

csp_logs = []

# -----------------------------------------------------------
# Constraint Check
# -----------------------------------------------------------

def is_treatment_safe(treatment):

    for allergy in csp_patient["allergies"]:

        if treatment.lower() == allergy.lower():

            csp_logs.append(
                f"[REJECTED] {treatment} — "
                f"Patient is allergic to {allergy}."
            )

            return False

    return True

# -----------------------------------------------------------
# Forward Checking
# -----------------------------------------------------------

def forward_checking_viral(domains):

    print("\nForward Checking Results:\n")

    valid_domains = {}

    for disease, treatments in domains.items():

        safe = [t for t in treatments if is_treatment_safe(t)]

        valid_domains[disease] = safe

        print(f"  {disease} -> {safe}")

    return valid_domains

# -----------------------------------------------------------
# MRV Heuristic
# -----------------------------------------------------------

def mrv_heuristic(domains):

    selected = min(domains, key=lambda d: len(domains[d]))
    return selected

# -----------------------------------------------------------
# Degree Heuristic
# -----------------------------------------------------------

def degree_heuristic_viral(domains):

    selected = max(domains, key=lambda d: len(domains[d]))
    return selected

# -----------------------------------------------------------
# LCV Heuristic
# -----------------------------------------------------------

def lcv_order(values):

    return sorted(values)

# -----------------------------------------------------------
# Backtracking
# -----------------------------------------------------------

def backtracking_csp(assignment, domains):

    if len(domains) == 0:
        return assignment

    variable = mrv_heuristic(domains)

    ordered_values = lcv_order(domains[variable])

    for value in ordered_values:

        if is_treatment_safe(value):

            assignment[variable] = value

            csp_logs.append(
                f"[ASSIGNED] {value} -> {variable}"
            )

            reduced = {
                k: v for k, v in domains.items()
                if k != variable
            }

            result = backtracking_csp(assignment, reduced)

            if result is not None:
                return result

            csp_logs.append(
                f"[BACKTRACK] Removing {value} from {variable}"
            )

            assignment.pop(variable)

    return None

# -----------------------------------------------------------
# Min-Conflicts
# -----------------------------------------------------------

def min_conflicts_viral(domains, max_steps=50):

    current = {
        d: random.choice(t)
        for d, t in domains.items()
    }

    for _ in range(max_steps):

        conflicts = [
            d for d, v in current.items()
            if not is_treatment_safe(v)
        ]

        if not conflicts:
            return current

        var = random.choice(conflicts)

        valid_vals = [
            v for v in domains[var]
            if is_treatment_safe(v)
        ]

        if valid_vals:
            current[var] = random.choice(valid_vals)

    return current

# -----------------------------------------------------------
# Appointment Scheduling
# -----------------------------------------------------------

appointments = {
    "Sneha Reddy":  "9:00 AM",
    "Ravi Kumar":   "10:30 AM",
    "Anita Sharma": "12:00 PM",
    "Mohammed Ali": "2:00 PM"
}

# -----------------------------------------------------------
# SAT Logic Check
# -----------------------------------------------------------

def sat_viral_check(symptoms):

    high_fever = "high_fever" in symptoms
    chills     = "chills" in symptoms
    sweating   = "sweating" in symptoms

    # fever AND chills AND sweating -> Malaria suspected
    if high_fever and chills and sweating:
        return "SAT Result: Malaria Suspected"

    if high_fever and chills:
        return "SAT Result: Possible Viral Infection"

    return "SAT Result: No Strong Match"

# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("\n" + "=" * 50)
print("VIRAL & INFECTIOUS DISEASE DIAGNOSIS ENGINE")
print("CO3 - CONSTRAINT SATISFACTION PROBLEM")
print("=" * 50)

print(f"\nPatient: {csp_patient['name']} | "
      f"Age: {csp_patient['age']} | "
      f"Gender: {csp_patient['gender']}")

print(f"Allergies: {csp_patient['allergies']}")

# Forward Checking
filtered = forward_checking_viral(treatment_variables)

# MRV
print(f"\nMRV Selected Variable: {mrv_heuristic(filtered)}")

# Degree
print(f"Degree Heuristic Variable: {degree_heuristic_viral(filtered)}")

# Backtracking
print("\nBacktracking Solution:\n")
bt_solution = backtracking_csp({}, filtered)
print(bt_solution)

# Min-Conflicts
print("\nMin-Conflicts Solution:\n")
mc_solution = min_conflicts_viral(filtered)
print(mc_solution)

# Scheduling
print("\nAppointment Scheduling:\n")
for pname, slot in appointments.items():
    print(f"  {pname} -> {slot}")

# SAT Check
print(f"\n{sat_viral_check(csp_patient['symptoms'])}")

# Logs
print("\nConstraint Logs:\n")
for log in csp_logs:
    print(f"  {log}")

print("\n" + "=" * 50)
print("CSP PROCESS COMPLETED")
print("=" * 50)

