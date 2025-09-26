from datetime import datetime, timedelta 


def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))





def calculate_future_date():
    number_of_days = int(input("Enter number of days to add to the current date:"))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
