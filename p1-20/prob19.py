
# How many Sundays fell on the first of the month during the 
# twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date, timedelta

# *****sunday = 6*********
start = date(1901, 1, 1)
end = date(2001, 1, 1)
delta = end - start
days = delta.days

next = timedelta(days=1)
d = start
first_sundays = 0
for day in range(days):
    if d.weekday() == 6 and d.day == 1:
        first_sundays += 1
    d = d + next

print("firsts and sundays: ", first_sundays)
