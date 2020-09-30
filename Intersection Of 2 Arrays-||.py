class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        m=len(nums2)
        num2countsmall = dict()
        num2countlarge = dict()
        temp = []
        if m<n:
            small = nums2
            large = nums1
        else:
            small = nums1
            large = nums2
        
        for i in range(len(small)):
            if small[i] not in num2countsmall:
                num2countsmall[small[i]] = 1
            else:
                num2countsmall[small[i]] += 1
        #print(num2countsmall)
        
        for i in range(len(large)):
            if large[i] not in num2countlarge:
                num2countlarge[large[i]] = 1
            else:
                num2countlarge[large[i]] += 1
        #print(num2countlarge)
        
        
        for key in num2countsmall:
            if key in num2countlarge:
                int_idx = min(num2countsmall[key],num2countlarge[key])
                #print(key,int_idx)
                temp.extend([key]*int_idx)
        #print(temp)        
        
        return temp
