def check_valid(pick,dest):
    areas=['a','b','c','d','e']
    flag=0
    if(pick!=dest):
        if(pick in areas and dest in areas):
            flag=1
    if(flag==0):
        print("\nError in Address part")
    return flag
def taxiavail(arr):
    flag=0
    for i in arr:
        if(i==0):
            flag=1
            break
    if(flag==0):
        print("\nTaxi unavailable...")
    return flag
def taxi(avail,prof):
    curr_avail=[]
    for i in range(0,numoftaxi):
        if(avail[i]==0):
            curr_avail.append(i)
    low=prof[curr_avail[0]]
    for i in curr_avail:
        if(prof[i]<low):
            low=prof[i]
    for i in curr_avail:
        if(low==prof[i]):
            return i
def cal_amount(pick,dest):
    areas=['a','b','c','d','e']
    for i in range(0,numoftaxi):
        if(pick==areas[i]):
            p=i
        if(dest==areas[i]):
            d=i
    sum1=p-d
    if(sum1<0):
        sum1=sum1*(-1)
    dis=sum1*15
    if(dis<5):
        amount=500;
    else:
        dis=dis-5
        amount=dis*10
        amount=amount+500
    return amount

print("Taxi Booking welcomes u")
numoftaxi=5
taxi_avail=[]
taxi_profit=[0,7,0,5,0]
for i in range(0,numoftaxi):
    taxi_avail.append(0)
    #taxi_profit.append(0)
book=input("Need Taxi(y/n): ")
while(book!="n"):
    print("Enter Pickup point: ",end='')
    pickup=input()
    print("Enter Destination point: ",end='')
    destin=input()
    if(check_valid(pickup,destin) and taxiavail(taxi_avail)):
        taxi_ind=taxi(taxi_avail,taxi_profit)
        taxi_avail[taxi_ind]=1
        profit=cal_amount(pickup,destin)
        taxi_profit[taxi_ind]=taxi_profit[taxi_ind]+profit
        print("\nTaxi Booked!!!\nTaxi name: Taxi",taxi_ind+1,"\nCost: ",profit,sep='')
        sum1=0
        for i in taxi_avail:
            sum1=sum1+i;
        if(sum1==numoftaxi):
            taxi_avail=[]
            dec=input("\nAll taxi are filled... Should we refresh all taxi's...(y/n): ")
            if(dec=="y"):
                for i in range(0,numoftaxi):
                    taxi_avail.append(0)
        print("\nThank for Booking. Need another booking...(y/n): ")
        book=input()
    else:
        print("Forbidden error has occured :(\nWould you like to come again...(y/n)")
        book=input()
print("\nWe are happy to serve you again... ^_^")
