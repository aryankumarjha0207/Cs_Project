class MedicationReminder:
    def __init__(self):
        self.medications = []

    def add_medication(self, name, dosage, time):
        med = {
            "name": name,
            "dosage": dosage,
            "time": time
        }
        self.medications.append(med)
        print(f"Added {name} at {time}")

    def remove_medications(self, name):
        for med in self.medications:
            if med['name'] == name:
                self.medications.remove(med)
                print(f"Removed {name}")
                return
        print(f"{name} not found")

    def list_medications(self):
        if not self.medications:
            print("\nNo medications added yet.")
            return
        
        print("\n" + "="*50)
        print("YOUR MEDICATIONS")
        print("="*50)
        for i, med in enumerate(self.medications, 1):
            print(f"{i}. {med['name']} - {med['dosage']} at {med['time']}")
        print("="*50 + "\n")

    def check_reminder(self, current_time):
        for med in self.medications:
            if med["time"] == current_time:
                print(f"\n*REMINDER: Take your {med['name']} ({med['dosage']}) NOW!*\n")

def main():
    reminder = MedicationReminder()
    
    while True:
        print("\n" + "="*50)
        print("1. Add medication")
        print("2. Remove medication")
        print("3. List all medications")
        print("4. Check reminder (enter time)")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ")

        if choice == '1':
            name = input("Medication name: ")
            dosage = input("Dosage: ")
            time = input("Time (HH:MM): ")
            reminder.add_medication(name, dosage, time)

        elif choice == '2':
            name = input("Medication name to remove: ")
            reminder.remove_medications(name)

        elif choice == '3':
            reminder.list_medications()

        elif choice == '4':
            current_time = input("Enter current time (HH:MM): ")
            reminder.check_reminder(current_time)

        elif choice == '5':
            print("\nStay Healthy!")
            break

        else:
            print("Invalid choice.")

main()
