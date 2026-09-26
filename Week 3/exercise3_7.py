year = int(input("Enter year: "))
month = int(input("Enter month: "))
if year>=1 and month>=1 and month <=12:
    Month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
            
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        Month[2]=29
    day =int(input("Enter day : "))
    if day>Month[month] or day<1:
        print("Invalid date")
    else :
        print("Valid date")

else:
    print("Invalid date")


#OUTPUT
#Enter year: 2007
#Enter month: 2
#Enter day : 29
#Invalid date

#Enter year: 2008
#Enter month: 2
#Enter day : 29
#Valid date
