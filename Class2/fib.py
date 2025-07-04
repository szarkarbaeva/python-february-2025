limit=int(input("Enter the number: "))

first=0
second=1
print(first)
print(second)
next = first + second

while next < limit:
    print(next)
    first=second
    second=next
    next=first+second

#0 1 1 2

#first= 0
#second= 1
#next = 1

#first


#0 11 2 3 5 13 21 34 55 89 144 233