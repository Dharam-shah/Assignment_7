def timetable(n, time=1):
    if time <= 12:
        print(n, time, n*time)
        timetable(n, time+1)
    else:
        return

timetable(int(input('Enter Number:')))