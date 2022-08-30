years = 2000-1901
thirty = ["april", "june", "september", "november"]
thirty_one = ["january", "march", "may", "july", "august", "october" "december"] 
february = 28
february_leap = 29
months = ["jan", "feb", "march", "april", "may", "june", "july", "aug", "sep", "oct", "nov", "december"]

days = ["tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday"]
first_sunday = 0
day = 0
sunday_count = 0
def is_leap(year):
    leap = True
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False

for year in range(1901,2001):
    leap = is_leap(year)
    for month in months:
        dayName = days[day%7]
        if dayName == "sunday":
            sunday_count += 1
        day += months[month]
        if leap == True and month == "february":
            day += 1

print(sunday_count)
    
