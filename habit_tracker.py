from database import add_habit, mark_habit_completed, get_all_habits, get_habit_completion

class HabitTracker:
    def __init__(self):
        print("Welcome to the Habit Tracker!")
        self.main_menu()

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Add a new habit")
            print("2. Mark habit as completed")
            print("3. View all habits")
            print("4. View habit completion history")
            print("5. Exit")

            choice = input("Choose an option (1-5): ")

            if choice == "1":
                self.add_new_habit()
            elif choice == "2":
                self.mark_habit_complete()
            elif choice == "3":
                self.view_all_habits()
            elif choice == "4":
                self.view_habit_history()
            elif choice == "5":
                print("Exiting Habit Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def add_new_habit(self):
        habit_name = input("Enter the habit name: ")
        description = input("Enter a short description for the habit: ")
        add_habit(habit_name, description)
        print(f"Habit '{habit_name}' added successfully!")

    def mark_habit_complete(self):
        self.view_all_habits()
        habit_id = input("Enter the Habit ID to mark as completed: ")

        if habit_id.isdigit():
            mark_habit_completed(int(habit_id))
            print(f"Habit with ID {habit_id} marked as completed for today!")
        else:
            print("Invalid Habit ID.")

    def view_all_habits(self):
        habits = get_all_habits()
        if habits:
            print("\nList of Habits:")
            print("ID | Habit Name | Start Date | Description")
            print("-" * 50)
            for habit in habits:
                print(f"{habit[0]} | {habit[1]} | {habit[2]} | {habit[3]}")
        else:
            print("No habits found. Add some to get started!")

    def view_habit_history(self):
        self.view_all_habits()
        habit_id = input("Enter the Habit ID to view its completion history: ")

        if habit_id.isdigit():
            history = get_habit_completion(int(habit_id))
            if history:
                print("\nCompletion History:")
                print("Date       | Completed")
                print("-" * 25)
                for entry in history:
                    date = entry[2]
                    status = "Yes" if entry[3] else "No"
                    print(f"{date} | {status}")
            else:
                print("No completion history found for this habit.")
        else:
            print("Invalid Habit ID.")
