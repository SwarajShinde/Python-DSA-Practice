def threeSum(self, nums: List[int]) -> List[List[int]]:
      """
      Hash set approach didnt work :( , not treid)
      use sort and 2 pointers
      """
      nums.sort()

      arr = set()

      for i in range(len(nums)):
          curr_val = nums[i]
          left = i+1
          right = len(nums)-1
          target_val = 0-curr_val
          while left<right:
              effec_val = nums[left]+nums[right]
              if effec_val==target_val:
                  arr.add((curr_val,nums[left],nums[right]))
                  left+=1
                  right-=1
              elif effec_val<target_val:
                  left+=1
              else:
                  right-=1

      return list(arr)

    
   
