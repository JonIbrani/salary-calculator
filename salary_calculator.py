print("This program calculates you salary.")
print("This program is designed with the assumption that you have a standard job with a consistent 40-hour workweek.")
pay_regular_hours = float(input("Type how much is they pay for hour in regular time schedule:\n"))
hours_worked = float(input("Type the numbers of hours you work on a week:\n" ))


if hours_worked > 40:
    print((pay_regular_hours * 40) + ((hours_worked - 40) * (1.5 * pay_regular_hours)))
else:
    print(hours_worked * pay_regular_hours)
    




