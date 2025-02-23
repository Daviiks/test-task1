import datetime as dt

def my_time():
    today = dt.datetime.now()
    weekday = today.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(f"Today is: {days[weekday]}")
    june_date = dt.datetime(2025, 6, 1)
    result = june_date - today
    print('Task 6')
    print(f"Current data: {today.date()}")
    print(f"Current time: {today.time()}")
    print(f"Days left until June 1, 2025 {result.days}")
    print('------------')


