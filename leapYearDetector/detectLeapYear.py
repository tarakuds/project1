year = int(input('What calender year will you like to check? '))
def isLeapYear(year):
    if (year%4==0):
        if (year%100 != 0):
            print(format(year) + ' is a leap year')
        elif (year%100 == 0):
            if(year%400 == 0):
                print(format(year) + ' is a leap year')
            else:
                print(format(year) + ' is not a leap year ')     
    else:
        print(format(year) + ' is not a leap year')

isLeapYear(year)

#Longer method
# year = 3002

# if (year%4==0):
#     if (year%100==0) and (year%400==0):
#         print(str(year) + 'is a leap year')
#     elif (year%100 != 0):
#         print(str(year) + 'is a leap year')
#     else:
#         print(str(year) + 'is not a leap year')
# else:
#     print(str(year) + 'is not a leap year')

