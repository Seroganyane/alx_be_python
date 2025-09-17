Task = input("Enter your task: ")
Priority = input("Priority (low, medium, high): ")
Time_bound = input("Is it time-bound? (yes/no): ")
match Priority:
    case "low":
        if Time_bound.lower() == "yes":
            print(f"Task '{Task}' is set with low priority and is time-bound.")
        else:
            print(f"Note: {Task} is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if Time_bound.lower() == "yes":
            print(f"Reminder: {Task} is a medium priority task that requires attention today!")
        else:
            print(f"Task '{Task}' is set with medium priority and is not time-bound.")
    case "high":
        if Time_bound.lower() == "yes":
            print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Task '{Task}' is set with high priority and is not time-bound.")
    case _:
        print("Invalid priority level. Please enter low, medium, or high.")
