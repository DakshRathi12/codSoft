# Task 1: To-Do List Application
todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Demo run with sample actions
# Simulating adding 2 tasks and showing them

todo_list.append("Complete Python Task")
todo_list.append("Attend Meeting at 5 PM")

print("\nDemo Run of To-Do List App")
show_menu()
print("\nAdding tasks...")
for i, task in enumerate(todo_list, 1):
    print(f"{i}. {task}")