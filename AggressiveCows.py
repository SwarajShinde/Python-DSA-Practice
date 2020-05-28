t=int(input())
for _ in range(t):
    n,c = map(int,input().split())
    temp=[]
    temp.sort()
    for i in range(n):
        a=int(input())
        temp.append(a)
    
    def F(x,arr,c):
        temp.sort()
        cowplaced = 1
        lastpos=temp[0]
        for i in range(n):
            if (temp[i]-lastpos >= x):
                cowplaced += 1
                lastpos = temp[i]
                if cowplaced == c:
                    return 1
        return 0
       

    
    def bin_search(arr,n):
        arr.sort()
        low = temp[0]
        high = temp[-1]-low

        while low<=high:
            mid = (low+high)//2
            if (F(mid,temp,c) == 1) and (F(mid+1,temp,c) == 0) :
                return mid
            elif F(mid,temp,c) == 1:
                low = mid+1
            elif F(mid,temp,c) == 0:
                high=mid-1
        return 0
    



print (bin_search(temp,n))
