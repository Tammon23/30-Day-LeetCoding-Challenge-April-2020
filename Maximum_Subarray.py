class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = max(nums)
      
        curSum = nums[0]
        curMax = nums[0]
        
        for num in nums[1:]:
            curSum = max(curSum+num, num)
            curMax = max(curMax, curSum)
            
        return curMax
