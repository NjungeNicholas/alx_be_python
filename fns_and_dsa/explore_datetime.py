from datetime import datetime, timedelta


# Function to display the current date and time
def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date

#Display current date and time
print(f"Current Date and time: {display_current_datetime()}")

# Function to add a specified number of days to the current date
number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')
print(f"Future date: {calculate_future_date(number_of_days)}")