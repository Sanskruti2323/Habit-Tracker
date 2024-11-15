from habit_tracker import HabitTracker
from gui import run_gui

def main():
    print("Welcome to Habit Tracker!")
    print("1. Start in Command Line Interface (CLI)")
    print("2. Start in Graphical User Interface (GUI)")
    choice = input("Choose an option (1-2): ")

    if choice == "1":
        HabitTracker()
    elif choice == "2":
        run_gui()
    else:
        print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
