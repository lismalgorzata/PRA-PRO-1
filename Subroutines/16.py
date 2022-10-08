import calendar

def month(n):
    for i in range(1,13):
      n=calendar.month_name[n]
      return n
n=7
nazwa=month(n)
print(nazwa)