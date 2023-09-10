def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)

number=int(input("enter a value : "))
res=fact_rec(number)
print("the factorial of {} is {}.".format(number,res))




# leapyear
def isLeapYear(year):
  if((year % 400 == 0) and (year % 100 != 0) or (year % 4 == 0)):
    return true
  else:
    return false

year=int(input("enter a year : "))
if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))
  

