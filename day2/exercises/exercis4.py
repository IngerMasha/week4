import datetime

def time_left_until_january_1st():
    current_datetime = datetime.datetime.now()
    january_1st_next_year = datetime.datetime(current_datetime.year + 1, 1, 1)
    time_difference = january_1st_next_year - current_datetime
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"January 1st will be in {days} days and {hours:02}:{minutes:02}:{seconds:02} hour.")

def display_current_date():
    current_date = datetime.datetime.now().date()
    print("Current date:", current_date)
    print("Current date (DD/MM/YYYY):", current_date.strftime("%d/%m/%Y"))
    print("Current date (YYYY-MM-DD HH:MM:SS):", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

import datetime

def minutes_lived(birthdate):
    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
    current_datetime = datetime.datetime.now()
    time_difference = current_datetime - birthdate
    minutes = time_difference.total_seconds() / 60
    print(f"You have lived {int(minutes)} minutes in your life.")
birthdate = "1990-05-20"
minutes_lived(birthdate)
print("\n")
display_current_date()
print("\n")

time_left_until_january_1st()
