task = input("Enter your task description: ")
priority = input("Enter the priority level (low, medium, high): ")
time_bound = input("Is this task time-bound? (yes/no): ")
match priority:
    case "low":
        if time_bound.lower() == "yes":
            print(f"Task '{task}' is set with low priority and is time-bound.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Task '{task}' is set with medium priority and is not time-bound.")
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Task '{task}' is set with high priority and is not time-bound.")
