class Patient:
    def __init__(self, name, age, gender, medical_history):
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_history = medical_history


class Medication:
    def __init__(self, name, daily_limit):
        self.name = name
        self.daily_limit = daily_limit


class Pharmacy:
    def __init__(self):
        self.patients = []
        self.medications = {}

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_medication(self, medication):
        self.medications[medication.name] = medication

    def sell_medication(self, patient_name, medication_name, dosage):
        patient = next((p for p in self.patients if p.name == patient_name), None)
        if not patient:
            print("Patient not found.")
            return

        medication = self.medications.get(medication_name)
        if not medication:
            print("Medication not found.")
            return

        if dosage <= medication.daily_limit:
            print(f"Sale successful. {dosage} mg of {medication_name} sold to {patient_name}.")
        else:
            print("Dosage exceeds daily limit. Sale not allowed.")


def main():
    pharmacy = Pharmacy()

    medication = Medication("Sacrosine", 1000)  # Adjust daily limit as needed
    pharmacy.add_medication(medication)

    patient = Patient("John Doe", 30, "Male", "Schizophrenia diagnosis")
    pharmacy.add_patient(patient)

    while True:
        print("\n1. Sell Medication")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            patient_name = input("Enter patient's name: ")
            medication_name = "Sacrosine"  # Assuming we're selling only sacrosine for now
            dosage = int(input("Enter the dosage in mg: "))
            pharmacy.sell_medication(patient_name, medication_name, dosage)
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
