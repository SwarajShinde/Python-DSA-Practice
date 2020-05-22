from collections import Counter
from heapq import heappop, heappush, heapify 
t=int(input())
for _ in range(t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    counts = Counter(arr)
    s=dict()
    for i in arr:
        s[i] = counts[i]

    lis = []
    for i in s:
        lis.append(s[i])
    
    heap = []
    heapify(heap)
   
    for i in lis:
        heappush(heap,-1*i)
    
    while m!=0:
        a=heappop(heap)
        a=a+1
        #keep on decreasing the value by 1 , until the value ==0 . THis is because we want the max number of Distinct elements.
        if a!=0:
            heappush(heap,a)
        
        m = m-1
    print(len(heap))

    
