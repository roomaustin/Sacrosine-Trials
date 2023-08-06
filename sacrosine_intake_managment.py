class Patient:
    def __init__(self, name, age, gender, medical_history):
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_history = medical_history
        self.sacrosine_daily_limit = 1000  # Adjust this based on medical recommendations
        self.sacrosine_intake = 0

    def take_sacrosine(self, dosage):
        if self.sacrosine_intake + dosage <= self.sacrosine_daily_limit:
            self.sacrosine_intake += dosage
            print(f"{dosage} mg of Sacrosine taken. Total intake: {self.sacrosine_intake} mg.")
        else:
            print("Daily limit exceeded. Consult a healthcare professional.")

    def get_remaining_limit(self):
        return self.sacrosine_daily_limit - self.sacrosine_intake


def main():
    patient_name = input("Enter patient's name: ")
    patient_age = int(input("Enter patient's age: "))
    patient_gender = input("Enter patient's gender: ")
    patient_medical_history = input("Enter patient's medical history: ")

    patient = Patient(patient_name, patient_age, patient_gender, patient_medical_history)

    while True:
        print("\n1. Take Sacrosine")
        print("2. Check remaining intake limit")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            dosage = int(input("Enter the dosage in mg: "))
            patient.take_sacrosine(dosage)
        elif choice == "2":
            remaining_limit = patient.get_remaining_limit()
            print(f"Remaining intake limit: {remaining_limit} mg")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
