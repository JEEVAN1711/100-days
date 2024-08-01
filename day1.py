In a park, they charge X rupees for adults and Y rupees for kids for entry. 
The program must accept two integers A and B as the input(where A is the number of adults and B is the number of kids). 
The program must print the total amount charged as the output.
ANSWER:
a,b=map(int,input().split())
x,y=map(int,input().split())
print(a*x+b*y)
