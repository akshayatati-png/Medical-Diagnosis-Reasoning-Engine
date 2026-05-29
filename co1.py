# ===========================================================
# CO1 - Intelligent Agent Model
# Viral & Infectious Disease Diagnosis Reasoning Engine
# ===========================================================

from dataclasses import dataclass
from typing import List, Dict

# -----------------------------------------------------------
# Patient Profile Representation
# -----------------------------------------------------------

@dataclass
class PatientProfile:
    name: str
    age: int
    gender: str
    symptoms: List[str]
    allergies: List[str]
    travel_history: str

# -----------------------------------------------------------
# Diagnosis Agent
# -----------------------------------------------------------

class InfectiousDiseaseAgent:

    def __init__(self):

        # Knowledge Base
        # Disease -> Symptoms

        self.knowledge_base: Dict[str, List[str]] = {

            "Dengue": [
                "high_fever",
                "severe_headache",
                "joint_pain",
                "skin_rash",
                "bleeding_gums"
            ],

            "Malaria": [
                "chills",
                "high_fever",
                "sweating",
                "nausea",
                "muscle_pain"
            ],

            "Typhoid": [
                "prolonged_fever",
                "abdominal_pain",
                "weakness",
                "loss_of_appetite",
                "constipation"
            ],

            "COVID-19": [
                "dry_cough",
                "high_fever",
                "loss_of_smell",
                "breathlessness",
                "fatigue"
            ],

            "Chikungunya": [
                "joint_pain",
                "skin_rash",
                "high_fever",
                "swollen_joints"
            ]
        }

    # -------------------------------------------------------
    # Diagnosis Function
    # -------------------------------------------------------

    def diagnose(self, patient: PatientProfile):

        possible_diseases = []

        print(f"\nPatient: {patient.name} | "
              f"Age: {patient.age} | "
              f"Gender: {patient.gender}")

        print(f"Travel History: {patient.travel_history}")
        print(f"\nSymptoms Reported: {patient.symptoms}\n")
        print("Scanning Knowledge Base...\n")

        for disease, symptoms in self.knowledge_base.items():

            match_count = 0

            print(f"Evaluating: {disease}")

            for symptom in symptoms:

                if symptom in patient.symptoms:

                    match_count += 1
                    print(f"  Matched: {symptom}")

            match_percentage = (match_count / len(symptoms)) * 100

            print(f"  Match Score: {match_count}/{len(symptoms)}"
                  f" ({match_percentage:.1f}%)\n")

            # If at least 2 symptoms match
            if match_count >= 2:
                possible_diseases.append(disease)

        return possible_diseases


# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("=" * 50)
print("VIRAL & INFECTIOUS DISEASE DIAGNOSIS ENGINE")
print("CO1 - INTELLIGENT AGENT MODEL")
print("=" * 50)

patient1 = PatientProfile(
    name="Ravi Kumar",
    age=28,
    gender="Male",
    symptoms=[
        "high_fever",
        "severe_headache",
        "joint_pain",
        "skin_rash"
    ],
    allergies=["aspirin"],
    travel_history="Returned from Kerala 5 days ago"
)

agent = InfectiousDiseaseAgent()
result = agent.diagnose(patient1)

print("-" * 50)
print("Possible Diseases Detected:")
print(result)
print("-" * 50)



