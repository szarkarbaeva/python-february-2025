years=int(input("Enter number of years: "))
choice=input("""
Select your choice:
1 - Days
2 - Weeks
3 - Hours
""")

if choice == "1": 
    print(f"In {years} years there are {365*years} days")
elif choice == "2":
    print(f"In {years} years there are {52*years} weeks")
elif choice == "3":
    print(f"In {years} years there are {365*24*years} hours")
else:
    print("select a right choice")

#print(years*365)

#print(f"In {years} years there are {365*years} days")
#print(f"In {years} years there are {52*years} weeks")
#print(f"In {years} years there are {365*24*years} hours")