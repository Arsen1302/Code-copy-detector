class Solution:
    def solution_441_2(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        result = [0] * l
        for i in range(l-1):
            for j in range(i+1, l):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
        return result