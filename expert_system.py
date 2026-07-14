# Expert System - Medical Diagnosis (Rule Based)

print("Answer the following questions with yes/no\n")

fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
cold = input("Do you have cold/runny nose? (yes/no): ").lower()
body_ache = input("Do you have body ache? (yes/no): ").lower()
sore_throat = input("Do you have sore throat? (yes/no): ").lower()
breathlessness = input("Do you have breathlessness? (yes/no): ").lower()
rashes = input("Do you have skin rashes? (yes/no): ").lower()
vomiting = input("Do you have vomiting? (yes/no): ").lower()

print("\n--- Diagnosis Result ---")

if fever == 'yes' and cough == 'yes' and breathlessness == 'yes':
    print("Possible Diagnosis: COVID-19 / Pneumonia")
    print("Advice: Get tested immediately, isolate, consult a doctor.")

elif fever == 'yes' and cold == 'yes' and sore_throat == 'yes':
    print("Possible Diagnosis: Common Cold / Flu")
    print("Advice: Rest, stay hydrated, take paracetamol if needed.")

elif fever == 'yes' and body_ache == 'yes' and rashes == 'yes':
    print("Possible Diagnosis: Dengue")
    print("Advice: Get a blood test done, avoid aspirin, consult doctor.")

elif fever == 'yes' and vomiting == 'yes' and body_ache == 'yes':
    print("Possible Diagnosis: Typhoid / Malaria")
    print("Advice: Get blood test done, consult doctor immediately.")

elif cough == 'yes' and sore_throat == 'yes' and fever == 'no':
    print("Possible Diagnosis: Mild Throat Infection")
    print("Advice: Warm water gargles, avoid cold drinks.")

elif fever == 'yes':
    print("Possible Diagnosis: Mild Viral Infection")
    print("Advice: Monitor temperature, rest, consult doctor if it persists.")

else:
    print("No significant symptoms detected / Insufficient data for diagnosis.")
    print("Advice: Consult a doctor if symptoms develop.")