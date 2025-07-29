class Solution:
    def solution_1383_4(self, answerKey: str, k: int) -> int:
        tmpK = k
        #check for False
        i = 0    
        for j in range(0,len(answerKey)):
            if answerKey[j] == 'T':
                k -= 1
            if k < 0:
                if answerKey[i] == 'T':
                    k += 1
                i += 1
        falseCount = j-i+1
        
        k = tmpK
        #check for True
        i = 0    
        for j in range(0,len(answerKey)):
            if answerKey[j] == 'F':
                k -= 1
            if k < 0:
                if answerKey[i] == 'F':
                    k += 1
                i += 1
        trueCount = j-i+1
        return max(falseCount, trueCount)