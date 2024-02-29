def get_season(month, day):
    if (month == "Mar" and day >= 20) or month in ("Apr", "May") or (month == "Jun" and day < 21):
        return "Spring"
    elif (month == "Jun" and day >= 21) or month in ("Jul", "Aug") or (month == "Sep" and day < 22):
        return "Summer"
    elif (month == "Sep" and day >= 22) or month in ("Oct", "Nov") or (month == "Dec" and day < 21):
        return "Fall"
    else:
        return "Winter"

# Get input from user
month_input = input("Enter the month: ").capitalize()
day_input = int(input("Enter the date: "))

# Get the first three letters of the month
month = month_input[:3]

# Check for the season
season = get_season(month, day_input)

# Display the result
print(f"The season associated with {month_input} {day_input} is {season}.")
