from datetime import date


today = date.today()
alexsBirthDay = date(today.year, 5, 8)
if alexsBirthDay < today:
    alexsBirthDay = alexsBirthDay.replace(year=today.year + 1)
timeTillBirthday = abs(alexsBirthDay - today)

# transform (PARSE) timetillbirthday.days to string (str)
print(str(timeTillBirthday.days) +  ' days')