import datetime

# Function to display the current date and time
def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date

#Display current date and time
print(f"Current Date and time: {display_current_datetime()}")

# Function to add a specified number of days to the current date
number_of_days = int(input("Enter the number of days to add: "))
def add_days_to_current_date(days):
    current_date = datetime.datetime.now()
    new_date = current_date + datetime.timedelta(days=days)
    return new_date
print(f"Future date: {add_days_to_current_date(number_of_days).strftime('%Y-%m-%d')}")