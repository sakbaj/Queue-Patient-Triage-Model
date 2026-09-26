print("================================")
print("      KGMU AI TRIAGE SYSTEM")
print("================================")

age = input("Enter patient age: ")
symptoms = input("Enter your symptoms: ")

patient = {
    "age": age,
    "symptoms": symptoms
}

# -----------------------------
# TRIAGE
# -----------------------------

symptoms_text = patient["symptoms"].lower()

if "chest pain" in symptoms_text:
    priority = "EMERGENCY"

elif "difficulty breathing" in symptoms_text:
    priority = "EMERGENCY"

elif "high fever" in symptoms_text:
    priority = "URGENT"

else:
    priority = "ROUTINE"


# -----------------------------
# RESULT
# -----------------------------

print("\n--- TRIAGE RESULT ---")
print("Age:", patient["age"])
print("Symptoms:", patient["symptoms"])
print("Priority:", priority)