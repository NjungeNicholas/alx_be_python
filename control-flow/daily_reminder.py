task = input("Enter today's task: ")
priority = input("Enter task priority (high/medium/low): ")
time_bound = input("Is this task time-bound? (yes/no): ")

match priority:
    case "high":
        message = f"HIGH priority: {task}"
    case "medium":
        message = f"MEDIUM priority: {task}"
    case "low":
        message = f"LOW priority: {task}"
    case _:
        message = task

if time_bound:
    message += " that requires immediate attention today!"
else:
    message += " — schedule it when convenient."

print("\n" + message)
