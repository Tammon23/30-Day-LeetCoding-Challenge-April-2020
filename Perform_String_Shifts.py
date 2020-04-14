class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        shift_amt = i = 0
        sLen = len(s)
        
        newString = [None for i in range(sLen)]
         
        for dire, amt in shift:
            if dire == 0:
                shift_amt -= amt
            else:
                shift_amt += amt
                
        while(i < sLen):
            newString[(i + shift_amt) % sLen] = s[i] 
            i += 1
            
        return ''.join(newString)
