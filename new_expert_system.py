# -------------------------------
# Knowledge Base
# -------------------------------

knowledge_base = {
    "car won't start": ("Dead Battery", "Recharge or Replace the Battery"),
    "engine overheating": ("Low Coolant", "Refill the Coolant"),
    "low tire pressure": ("Puncture or Air Leak", "Inflate or Repair the Tire"),
    "brake noise": ("Worn Brake Pads", "Replace the Brake Pads"),
    "headlights dim": ("Weak Battery", "Charge or Replace the Battery")
}


# -------------------------------
# Inference Engine
# -------------------------------

def inference_engine(symptom):
    if symptom in knowledge_base:
        return knowledge_base[symptom]
    else:
        return None


# -------------------------------
# User Interface
# -------------------------------

symptom = input("Enter the automobile problem: ").lower()

result = inference_engine(symptom)

if result:
    cause, solution = result
    print("\nPossible Cause :", cause)
    print("Suggested Solution :", solution)
else:
    print("\nSymptom not found in Knowledge Base.")