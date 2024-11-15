from database import get_habit_completion, get_all_habits
from datetime import datetime

class HabitReport:
    def __init__(self):
        pass

    def generate_report(self):
        habits = get_all_habits()
        if not habits:
            print("No habits found to generate a report.")
            return

        print("\nHabit Report:")
        for habit in habits:
            habit_id = habit[0]
            habit_name = habit[1]
            completion_history = get_habit_completion(habit_id)

            total_days = len(completion_history)
            completed_days = sum(1 for entry in completion_history if entry[3])

            streak = self.calculate_streak(completion_history)

            print(f"\nHabit: {habit_name}")
            print(f"Total Days Tracked: {total_days}")
            print(f"Completed Days: {completed_days}")
            print(f"Current Streak: {streak} days")

            if total_days > 0:
                completion_percentage = (completed_days / total_days) * 100
                print(f"Completion Rate: {completion_percentage:.2f}%")
            else:
                print("No completion data available yet.")

    def calculate_streak(self, completion_history):
        """Calculate the longest streak of consecutive completed days."""
        streak = 0
        max_streak = 0
        previous_date = None

        for entry in completion_history:
            if entry[3]:  # If habit was completed
                current_date = datetime.strptime(entry[2], '%Y-%m-%d').date()

                if previous_date and (current_date - previous_date).days == 1:
                    streak += 1
                else:
                    streak = 1

                max_streak = max(max_streak, streak)
                previous_date = current_date
            else:
                streak = 0

        return max_streak
