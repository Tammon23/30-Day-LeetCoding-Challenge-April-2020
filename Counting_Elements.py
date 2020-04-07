class Solution:
    def countElements(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 0
    
        counter = 0
        numCounts = {}
        for el in arr:
            if el in numCounts:
                numCounts[el] += 1
            else:
                numCounts[el] = 1

        for key in numCounts:
            if key+1 in numCounts:
                counter += numCounts[key]
                
        return counter
