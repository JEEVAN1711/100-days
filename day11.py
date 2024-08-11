a=float(input("enter first no "))
b=float(input("enter second no "))
c=float(input("enter third no "))
d=float(input("enter fourth no "))
if (a>b and a>c and a>d):
    print("greatest number is:",a)
elif (b>c and b>d):
    print("greatest number is:",b)
elif (c>d):
    print("greatest number is:",c)
elif (d>c):
    print("greatest number is:",d)
else:
    print("Either any two values or all the four values are equal")
