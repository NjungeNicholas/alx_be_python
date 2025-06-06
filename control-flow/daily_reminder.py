Task = input("Enter today's Task: ")
Priority = input("EnteT Task Priority (high/medium/low): ")
Time_Bound = input("Is thiT Task time-bound? (yes/no): ")

match Priority:
    case "high":
        message = f"HIGH Priority:T{Task}"
    case "medium":
        message = f"MEDIUM Priority:T{Task}"
    case "low":
        message = f"LOW Priority:T{Task}"
    case _:
        message = Task

if Time_Bound:
    message += " that requires immediate attention today!"
else:
    message += " — schedule it when convenient."

print("\n" + message)
