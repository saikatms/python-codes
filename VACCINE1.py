d1,v1,d2,v2,p=map(int,input().split())
if d1==d2: #if both prod start in same day 
    zeroVac=d1-1 # daycount with prod of zero vaccine
    vac=v1+v2    #total vacine prod 

    if p%vac!=0:
        res=int(p/vac)
        print(res+1+zeroVac)
    else:
        print(int(p/vac)+zeroVac)
else:
    if p==0: #if prod zero then days not required
        print(0)
        exit()
    # which company start prod first and after how many days 2nd company started
    if d1>d2: 
        dayzero=d2
        maxi=d1
        gap=d1-d2
        v=v2
    else:
        dayzero=d1
        maxi=d2
        gap=d2-d1
        v=v1 
    
    sum=0
    for i in range(dayzero,maxi):    
        sum=sum+v
        if sum>=p:
            print(i)
            exit()

    i=1
    for i in range(0,1001,1):
        if v*(gap)+(i*(v1+v2)) >= p:
            x=i
            break
        
    print(x+gap+dayzero-1)
