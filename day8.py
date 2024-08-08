The program must accept three integers X, Y and Z as the input. Two of these three integers will have same unit digit. 
The program must the print smallest integer among the integers which are having the same unit digit. 
Then the program must print the largest integer among the integers which are having the same unit digit. Finally, the program must print the remaining integer as the output.
x,y,z=map(int,input().split())
if(x%10)==(y%10):
    print(min(x,y),max(x,y),z)
elif(y%10)==(z%10):
    print(min(y,z),max(y,z),x)
elif(x%10)==(z%10):
    print(min(x,z),max(x,z),y)
