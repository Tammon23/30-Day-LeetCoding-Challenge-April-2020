import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        stones = [-stone for stone in stones]
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)    
            
            if x != y:
                diff = y - x
                heapq.heappush(stones, -diff)
        
        return -stones[0] if stones else 0
