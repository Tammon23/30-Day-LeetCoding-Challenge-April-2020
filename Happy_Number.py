class Solution:
    def getSumOfDigits(self, n: int) -> int:
        sum = 0
        while n > 0:
            sum += (n%10)**2
            n = int(n/10)
        return sum
        
    def isHappy(self, n: int) -> bool:
        if n < 0:
            return False
        
        visited = set()
        
        while(True):
            sumOfDigits = self.getSumOfDigits(n)
            if sumOfDigits == 1:
                return True
            
            if sumOfDigits in visited:
                return False
            
            visited.add(sumOfDigits)
            n = sumOfDigits
            
        
