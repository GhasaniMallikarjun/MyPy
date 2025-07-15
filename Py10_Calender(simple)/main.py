import calendar


def month_name_to_number(month_name):
    month_number=list(calendar.month_name).index(month_name)
    return month_number


date_input=input("Enter Month & Year (e.g., July, 2024): ")

month_name, year=date_input.split(", ")
year=int(year)

month_number=month_name_to_number(month_name)

print(calendar.month(year, month_number))
