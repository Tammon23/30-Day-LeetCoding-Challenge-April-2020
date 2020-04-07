class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
                
        curIndex = 0
        firstZeroIndex = 0
        
        while(curIndex < len(nums) and firstZeroIndex < len(nums)):
            
            # looking for earliest sighting of a zero
            while(nums[firstZeroIndex] != 0):
                firstZeroIndex += 1
                if firstZeroIndex >= len(nums) - 1:
                    return
            
            # swapping the curIndex with 0 if curIndex is not 0
            while(nums[curIndex] == 0):
                curIndex += 1
                if curIndex == len(nums):
                    return
            if firstZeroIndex < curIndex:
                nums[firstZeroIndex], nums[curIndex] = nums[curIndex], 0
                firstZeroIndex += 1
                
            curIndex += 1
            
        
        return
