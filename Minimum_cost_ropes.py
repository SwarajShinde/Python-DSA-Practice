import heapq
t=int(input())
for _ in range(t):
    m=int(input())
    arr = list(map(int,input().split()))
    cost = 0
   '''
    A basic question of priority queue implementation 
    heapify the array if len!=1 or 0 , then pop the elements and store them onto variable
   cost is the sum of the two
    if array still exists ie. len!=0 then append the a+b
   '''
   
    if not arr:
        print(-1)
    if len(arr)==1:
        print(arr[0])
    heapq.heapify(arr)
    while len(arr)>1:
        a,b = heapq.heappop(arr),heapq.heappop(arr)
        cost += (a+b)           
        
        if arr:
            heapq.heappush(arr,a+b)   # heap push maintains the heap invarient 
    print(cost)
        
        
        
