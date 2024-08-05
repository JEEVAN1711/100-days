five integers are passed as the input to the program.the program must print the count odd integers as the output
numlist=map(int,input().split())
count=0
for f in numlist:
  if(f%2)==1:
    count+=1
print(count)
