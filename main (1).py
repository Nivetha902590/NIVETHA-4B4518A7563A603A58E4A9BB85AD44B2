year=int(input("Ente any one year:"))
if year%4==0 and year%100!=0:
  print(year,"is a leap year")
elif year%100==10:
  print(year,"is not a leap year")
elif year%400==0:
  print(year,"is a leap year")
else:
  print(year,"is not a leap year") 

