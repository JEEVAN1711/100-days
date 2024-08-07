24 hours format change to 12 hours format 
a=(input())
hours,minute=((a[0:2])),(a[2:4])
if(int(hours))==0 and (minute)=='00':
    print("12:00" ,"AM")
elif(int(hours)==12 and int(minutes)>0):
    print(f"{hours}:{minutes} PM")
elif(int(hours))<12:
    print(f"{hours}:{minute} AM")
else:
    hours=int(hours)
    if((hours)<22):
        print(f"0{hours-12}",end="")
    else:
        print(f"{hours-12}",end="")
      
    print(f":{minute} PM")
