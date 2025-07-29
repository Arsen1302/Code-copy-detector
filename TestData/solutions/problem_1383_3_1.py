class Solution:
    def solution_1383_3_1(self, answerKey: str, k: int) -> int:
        ifTrueIsAnswer = self.solution_1383_3_2(answerKey, k, "T")
        ifFalseIsAnswer = self.solution_1383_3_2(answerKey, k, "F")
        return max(ifTrueIsAnswer, ifFalseIsAnswer)
    
    def solution_1383_3_2(self, array, k, key):
        left, result = 0, 0
        for right in range(len(array)):
            if array[right] == key:
                k -= 1
            if k < 0:
                result = max(result, right-left)
                while k < 0:
                    if array[left] == key:
                        k += 1
                    left += 1
        return max(result, right+1-left)