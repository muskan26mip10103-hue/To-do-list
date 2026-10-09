# A task starts with Pending status and can later become Completed.
# Task numbers are updated after individual or bulk deletion.
# Searches ignore capitalization in titles and categories.
# The menu repeats until the user chooses the Exit option.
# ================================================================
#              TO-DO LIST MANAGEMENT SYSTEM
# ================================================================
# Manage tasks with beginner Python concepts: lists, dictionaries,
# functions, loops, conditions, input, output, and counting.
# Features include adding, viewing, updating, deleting, searching,
# priority selection, status filters, and completion summaries.
# ================================================================

# This list stores task dictionaries while the program is running.
tasks = []

# Display the project title when the program starts.
def display_title():
    """Display the application title."""
    print("=" * 52)
    print("        TO-DO LIST MANAGEMENT SYSTEM")
    print("=" * 52)
    print("                 PYTHON MINI PROJECT")
    print("=" * 52)
    print()

def display_introduction():
    """Explain the program to the user."""
    print("Welcome to the To-Do List Management System.")
    print("Use the menu to organize your tasks.")
    print("Each task has a number, title, category, priority,")
    print("and status.")
    print()

def get_user_name():
    """Ask for a name and return a default if it is blank."""
    name = input("Enter your name: ").strip()
    if name == "":
        print("No name was entered, so the name User will be used.")
        name = "User"
    return name

def get_non_empty_text(prompt):
    """Keep asking until the user enters non-empty text."""
    value = input(prompt).strip()
    while value == "":
        print("This value cannot be empty.")
        value = input(prompt).strip()

    return value

def get_task_number(prompt):
    """Read a positive task number from the user."""
    number_text = input(prompt).strip()
    while not number_text.isdigit() or int(number_text) < 1:
        print("Enter a positive whole number.")
        number_text = input(prompt).strip()

    return int(number_text)

def choose_priority():
    """Ask the user to choose a task priority."""
    print()
    print("Choose a priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")
    choice = input("Enter priority choice: ").strip()

    while choice not in ["1", "2", "3"]:
        print("Choose 1, 2, or 3.")
        choice = input("Enter priority choice: ").strip()
    if choice == "1":
        return "High"
    elif choice == "2":
        return "Medium"
    else:
        return "Low"

def create_task(title, category, priority):
    """Create a task dictionary and return it."""
    task = {
        "number": len(tasks) + 1,
        "title": title,
        "category": category,
        "priority": priority,
        "status": "Pending"
    }

    return task

def add_task():
    """Ask for task information and save a new task."""
    print()
    print("---------------- ADD TASK ----------------")
    title = get_non_empty_text("Enter the task: ")
    category = get_non_empty_text("Enter a category: ")
    priority = choose_priority()

    new_task = create_task(title, category, priority)
    tasks.append(new_task)
    print()
    print("Task added successfully.")
    print_task(new_task)
    print()

def print_task(task):
    """Print the fields of one task in a consistent format."""
    print("Task Number :", task["number"])
    print("Task Name   :", task["title"])
    print("Category    :", task["category"])
    print("Priority    :", task["priority"])
    print("Status      :", task["status"])
    print("-" * 45)

def display_tasks():
    """Display every task."""
    print()
    print("---------------- ALL TASKS ----------------")

    if len(tasks) == 0:
        print("There are no tasks.")
        print()
        return
    print("Total tasks:", len(tasks))
    print()

    for task in tasks:
        print_task(task)
    print()

def find_task(task_number):
    """Return the matching task dictionary, or None."""
    for task in tasks:
        if task["number"] == task_number:
            return task

    return None

def show_task_not_found():
    """Print a standard message when a task is missing."""
    print("Task number not found.")
    print()

def ask_for_existing_task():
    """Ask for a task number and return the matching task."""
    if len(tasks) == 0:
        print("There are no tasks available.")
        return None
    display_tasks()
    number = get_task_number("Enter a task number: ")
    task = find_task(number)

    if task is None:
        show_task_not_found()
    return task

def complete_task():
    """Change a pending task's status to Completed."""
    print()
    print("---------------- COMPLETE TASK ----------------")

    task = ask_for_existing_task()
    if task is None:
        return

    if task["status"] == "Completed":
        print("This task is already completed.")
    else:
        task["status"] = "Completed"
        print("Task marked as completed.")
        print_task(task)
    print()

def update_task():
    """Update the title, category, or priority of a task."""
    print()
    print("---------------- UPDATE TASK ----------------")

    task = ask_for_existing_task()
    if task is None:
        return

    print("Current task:")
    print_task(task)
    print("What would you like to update?")
    print("1. Task title")
    print("2. Category")
    print("3. Priority")
    print("4. Cancel")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        task["title"] = get_non_empty_text("Enter the new title: ")
        print("Task title updated.")
    elif choice == "2":
        task["category"] = get_non_empty_text("Enter the new category: ")
        print("Category updated.")
    elif choice == "3":
        task["priority"] = choose_priority()
        print("Priority updated.")
    elif choice == "4":
        print("Update cancelled.")
    else:
        print("Invalid update choice.")
    print()

def delete_task():
    """Remove one selected task from the list."""
    print()
    print("---------------- DELETE TASK ----------------")

    task = ask_for_existing_task()
    if task is None:
        return

    removed_title = task["title"]
    tasks.remove(task)
    renumber_tasks()
    print("Task deleted:", removed_title)
    print()

def renumber_tasks():
    """Give tasks consecutive numbers after a deletion."""
    number = 1

    for task in tasks:
        task["number"] = number
        number = number + 1

def count_tasks():
    """Display and return the total task count."""
    total = len(tasks)
    print()
    print("---------------- TASK COUNT ----------------")
    print("Total tasks:", total)
    print()

    return total

def count_tasks_with_status(status):
    """Count tasks whose status matches the given value."""
    count = 0
    for task in tasks:
        if task["status"] == status:
            count = count + 1

    return count

def count_pending_tasks():
    """Display the number of pending tasks."""
    pending = count_tasks_with_status("Pending")
    print()
    print("Pending tasks:", pending)
    print()

    return pending

def count_completed_tasks():
    """Display the number of completed tasks."""
    completed = count_tasks_with_status("Completed")
    print()
    print("Completed tasks:", completed)
    print()

    return completed

def display_tasks_with_status(status):
    """Display tasks matching a status."""
    print()
    print("----------------", status.upper(), "TASKS ----------------")
    matching_count = 0

    for task in tasks:
        if task["status"] == status:
            print_task(task)
            matching_count = matching_count + 1
    if matching_count == 0:
        print("There are no", status.lower(), "tasks.")

    print("Total", status.lower(), "tasks:", matching_count)
    print()

def display_pending_tasks():
    """Display only pending tasks."""
    display_tasks_with_status("Pending")

def display_completed_tasks():
    """Display only completed tasks."""
    display_tasks_with_status("Completed")

def display_tasks_by_priority(priority):
    """Display tasks that have the selected priority."""
    print()
    print("----------------", priority.upper(), "PRIORITY TASKS ----------------")
    matching_count = 0

    for task in tasks:
        if task["priority"] == priority:
            print_task(task)
            matching_count = matching_count + 1
    if matching_count == 0:
        print("There are no", priority.lower(), "priority tasks.")

    print("Matching tasks:", matching_count)
    print()

def filter_tasks_by_priority():
    """Let the user select a priority filter."""
    print()
    print("---------------- FILTER BY PRIORITY ----------------")
    priority = choose_priority()
    display_tasks_by_priority(priority)

def search_tasks():
    """Find tasks whose title or category contains a word."""
    print()
    print("---------------- SEARCH TASKS ----------------")
    if len(tasks) == 0:
        print("There are no tasks to search.")
        print()
        return

    search_text = get_non_empty_text("Enter a word to search for: ")
    search_text = search_text.lower()
    found_count = 0
    for task in tasks:
        title_matches = search_text in task["title"].lower()
        category_matches = search_text in task["category"].lower()

        if title_matches or category_matches:
            print_task(task)
            found_count = found_count + 1
    if found_count == 0:
        print("No tasks matched your search.")

    print("Matching tasks:", found_count)
    print()

def completion_percentage():
    """Calculate and display the completed-task percentage."""
    total = len(tasks)
    completed = count_tasks_with_status("Completed")
    print()
    print("---------------- COMPLETION ----------------")

    if total == 0:
        print("There are no tasks.")
        print("Completion percentage: 0%")
    else:
        percentage = completed * 100 / total
        print("Total tasks:", total)
        print("Completed tasks:", completed)
        print("Completion percentage:", round(percentage, 2), "%")
    print()

def remove_completed_tasks():
    """Remove all completed tasks from the list."""
    print()
    print("---------------- CLEAR COMPLETED TASKS ----------------")

    completed_count = count_tasks_with_status("Completed")
    if completed_count == 0:
        print("There are no completed tasks to remove.")
        print()
        return

    print("Completed tasks to remove:", completed_count)
    answer = input("Remove them? Enter Y to confirm: ").strip().lower()
    if answer == "y":
        remaining_tasks = []

        for task in tasks:
            if task["status"] != "Completed":
                remaining_tasks.append(task)
        tasks.clear()

        for task in remaining_tasks:
            tasks.append(task)
        renumber_tasks()
        print("Completed tasks removed.")
    else:
        print("No tasks were removed.")

    print()

def task_summary():
    """Display totals and completion percentage."""
    total = len(tasks)
    pending = count_tasks_with_status("Pending")
    completed = count_tasks_with_status("Completed")
    if total == 0:
        percentage = 0
    else:
        percentage = completed * 100 / total

    print()
    print("=" * 52)
    print("                  TASK SUMMARY")
    print("=" * 52)
    print("Total tasks     :", total)
    print("Pending tasks   :", pending)
    print("Completed tasks :", completed)
    print("Completion      :", round(percentage, 2), "%")
    print("=" * 52)
    print()

def display_menu():
    """Display all available commands."""
    print()
    print("=" * 52)
    print("MAIN MENU")
    print("=" * 52)
    print("1. Add Task")
    print("2. Display All Tasks")
    print("3. Count All Tasks")
    print("4. Count Pending Tasks")
    print("5. Count Completed Tasks")
    print("6. Complete a Task")
    print("7. Update a Task")
    print("8. Delete a Task")
    print("9. Display Pending Tasks")
    print("10. Display Completed Tasks")
    print("11. Search Tasks")
    print("12. Filter Tasks by Priority")
    print("13. Completion Percentage")
    print("14. Task Summary")
    print("15. Remove Completed Tasks")
    print("16. Exit")
    print("=" * 52)

def process_choice(choice):
    """Run the function selected by the user."""
    if choice == 1:
        add_task()
    elif choice == 2:
        display_tasks()
    elif choice == 3:
        count_tasks()
    elif choice == 4:
        count_pending_tasks()
    elif choice == 5:
        count_completed_tasks()
    elif choice == 6:
        complete_task()
    elif choice == 7:
        update_task()
    elif choice == 8:
        delete_task()
    elif choice == 9:
        display_pending_tasks()
    elif choice == 10:
        display_completed_tasks()
    elif choice == 11:
        search_tasks()
    elif choice == 12:
        filter_tasks_by_priority()
    elif choice == 13:
        completion_percentage()
    elif choice == 14:
        task_summary()
    elif choice == 15:
        remove_completed_tasks()
    elif choice == 16:
        print()
        print("Thank you for using the To-Do List.")
        print("Program closed successfully.")
        print()
        return False
    else:
        print()
        print("Invalid choice. Select a number from 1 to 16.")
        print()
    return True

def main():
    """Display the welcome screen and run the menu loop."""
    display_title()
    display_introduction()

    user_name = get_user_name()
    print()
    print("Hello", user_name + "!")
    print("Your To-Do List is ready.")

    running = True
    while running:
        display_menu()
        choice_text = input("Enter your choice: ").strip()

        if choice_text.isdigit():
            choice = int(choice_text)
            running = process_choice(choice)
        else:
            print()
            print("Please enter a valid whole number.")
            print()

# Start the program.
main()
# ================================================================
#                     END OF PROGRAM
# ================================================================




