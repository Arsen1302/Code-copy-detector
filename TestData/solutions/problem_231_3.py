class Solution:
    def solution_231_3(self, s: str, k: int) -> int:
        leftPointer = 0
        currentCharDict = {}
        longestLength = 0
        for rightPointer,rightValue in enumerate(s):
            leftValue = s[leftPointer]
            
            if rightValue not in currentCharDict:
                currentCharDict[rightValue] = 0
            currentCharDict[rightValue] += 1
            
            currentLength = rightPointer - leftPointer + 1
            if currentLength - max(currentCharDict.values()) <= k:
                longestLength = max(longestLength, currentLength)
            else:
                currentCharDict[leftValue] -= 1
                if currentCharDict[leftValue] == 0:
                    del currentCharDict[leftValue]
                leftPointer += 1
        return longestLength