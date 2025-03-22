year = int(input("Enter a year:- "))

if year % 4 == 0:   ## function check for 4
    if year % 100 == 0:  ## check for 100: before 2000 year
        if year % 400 == 0:  ## check for 400
            print(f"This year is leap year:- {year}")
        else:
            print(f"This year is not leap year:- {year}")
    else:
        print(f"This is Leap Year:- {year}")
else:
    print(f"This is not leap year:- {year}")