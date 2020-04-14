class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        subArrCounts = {0: -1}
        maxLen = curCount = 0
        
        for c, num in enumerate(nums):
            if not num:
                curCount += -1
            else:
                curCount += 1
                
            
            if curCount in subArrCounts:
                maxLen = max(c-subArrCounts[curCount], maxLen)
            
            else:
                subArrCounts[curCount] = c
            
            
        return maxLen
        
