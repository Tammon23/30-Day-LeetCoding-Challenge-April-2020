class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            anagramGroupLoc = {}
            result = []
            unique = 0

            for index, el in enumerate(strs):
                mWord = "".join(sorted(el))
                if mWord in anagramGroupLoc:
                    result[anagramGroupLoc[mWord]].append(strs[index])
                else:
                    anagramGroupLoc[mWord] = unique
                    result.append([strs[index]])
                    unique+= 1


            return (result)

