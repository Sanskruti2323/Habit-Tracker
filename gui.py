import tkinter as tk
from tkinter import messagebox
from database import add_habit, mark_habit_completed, get_all_habits, get_habit_completion
from reports import HabitReport

class HabitTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.root.geometry("400x400")

        # Habit Tracker Menu
        self.menu_label = tk.Label(self.root, text="Habit Tracker Menu", font=("Arial", 16))
        self.menu_label.pack(pady=10)

        self.add_habit_button = tk.Button(self.root, text="Add New Habit", command=self.add_new_habit)
        self.add_habit_button.pack(pady=5)

        self.mark_complete_button = tk.Button(self.root, text="Mark Habit as Completed", command=self.mark_habit_complete)
        self.mark_complete_button.pack(pady=5)

        self.view_habits_button = tk.Button(self.root, text="View All Habits", command=self.view_all_habits)
        self.view_habits_button.pack(pady=5)

        self.view_report_button = tk.Button(self.root, text="View Habit Report", command=self.view_report)
        self.view_report_button.pack(pady=5)

        self.quit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.quit_button.pack(pady=20)

    def add_new_habit(self):
        # Add new habit popup
        def save_habit():
            habit_name = habit_name_entry.get()
            description = description_entry.get()

            if habit_name and description:
                add_habit(habit_name, description)
                messagebox.showinfo("Success", f"Habit '{habit_name}' added successfully!")
                add_habit_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in both fields.")

        add_habit_window = tk.Toplevel(self.root)
        add_habit_window.title("Add New Habit")

        tk.Label(add_habit_window, text="Habit Name:").pack(pady=5)
        habit_name_entry = tk.Entry(add_habit_window)
        habit_name_entry.pack(pady=5)

        tk.Label(add_habit_window, text="Description:").pack(pady=5)
        description_entry = tk.Entry(add_habit_window)
        description_entry.pack(pady=5)

        save_button = tk.Button(add_habit_window, text="Save Habit", command=save_habit)
        save_button.pack(pady=10)

    def mark_habit_complete(self):
        # Mark habit completed popup
        def save_completion():
            habit_id = habit_id_entry.get()
            if habit_id.isdigit():
                mark_habit_completed(int(habit_id))
                messagebox.showinfo("Success", f"Habit with ID {habit_id} marked as completed!")
                mark_complete_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid Habit ID.")

        mark_complete_window = tk.Toplevel(self.root)
        mark_complete_window.title("Mark Habit Completed")

        tk.Label(mark_complete_window, text="Enter Habit ID:").pack(pady=5)
        habit_id_entry = tk.Entry(mark_complete_window)
        habit_id_entry.pack(pady=5)

        save_button = tk.Button(mark_complete_window, text="Mark Completed", command=save_completion)
        save_button.pack(pady=10)

    def view_all_habits(self):
        habits = get_all_habits()
        view_window = tk.Toplevel(self.root)
        view_window.title("View All Habits")

        if habits:
            for habit in habits:
                habit_text = f"ID: {habit[0]} | Name: {habit[1]} | Description: {habit[3]}"
                tk.Label(view_window, text=habit_text).pack(pady=2)
        else:
            tk.Label(view_window, text="No habits found. Please add some.").pack(pady=10)

    def view_report(self):
        report = HabitReport()
        report.generate_report()

def run_gui():
    root = tk.Tk()
    app = HabitTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
