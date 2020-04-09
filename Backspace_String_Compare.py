#Probably better to use stacks since it's a builtin
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        arrS = [None] * len(S)
        arrT = [None] * len(T)

        sPointer = tPointer = 0

        for char in S:
            if char == "#":
                if sPointer > 0:
                    sPointer -= 1
            else:
                arrS[sPointer] = char 
                sPointer += 1


        for char in T:
            if char == "#":
                if tPointer > 0:
                    tPointer -= 1
            else:
                arrT[tPointer] = char 
                tPointer += 1

        return arrS[0:sPointer] == arrT[0:tPointer]
