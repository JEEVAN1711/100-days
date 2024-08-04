take input as three integers and print one number is largest integer and smallest integer and sum as print the  output:
a,b,c=map(int,input().split())
print(min(min(a,b),c)+(max(max(a,b),c)))
