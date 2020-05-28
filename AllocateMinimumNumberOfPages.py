n=int(input())
m=int(input())
arr=list(map(int,input().split()))

# This function checks whether the given minimum pages by binary search are possible to be distributed with current number of students or not
def curr_min(arr,n,m,x):
    stud = 1
    curr_sum = 0
    for i in range(n):
        if arr[i]>x:
            return False
        if curr_sum + arr[i] > x:
            stud +=1
            curr_sum = arr[i]

            if stud>m:
                return False
        else:
            curr_sum += arr[i]

    return True

# Used Binary Search to find the minimum number of Pages to be read
def bin_search(arr,n,m):
    sum1=0
    if n<m:
        return -1
    for i in range(n):
        sum1 += arr[i]
    start = 0
    end = sum1
    result = 99999

    while start<end:
        mid = (start+end)//2
        if curr_min(arr,n,m,mid):
            result = min(result,mid)
            end = mid-1

        else:
            start = mid+1
    return result

print(bin_search(arr,n,m))
