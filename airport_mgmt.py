#codechef contest

with open('airport.txt','r') as f:
    T = f.readline()
    T = int(T)
    for i in range(T):
        print('i:',i)
        n = int(f.readline())#int(input()) #number of planes
        print("n:",n)
        planelist = list()
        #for j in range(n):
        arrivals = [int(x) for x in f.readline().split()]
        departures = [int(y) for y in f.readline().split()]
        print(arrivals,departures)
        for k in range(n):
            planelist.append([arrivals[k],departures[k]])#(range(arrivals[k],departures[k]+1)))
        print("planelist:",planelist)
        total_runways = 0
        for t in range(min(arrivals),max(departures)+1):
            print("t:",t)
            runways = sum([t in p for p in planelist])
            print("runways:",runways)
            total_runways = max(total_runways,runways)
            # for p in planelist:
            #     ts = 0
            #     if t in p:
            #         #print("t in p",p)
            #         ts += 1
            # runways = max(runways,ts)
        print("total",total_runways)