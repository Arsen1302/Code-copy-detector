class Solution:
    def solution_1620_2(self, nums: List[int], numsDivide: List[int]) -> int:
        counter = Counter(nums)
        setDivide = set(numsDivide)
        
        result = 0
        minimum = float("inf")
        
        for i in sorted(set(nums)):
            flag = True
            for k in setDivide:
                if k % i != 0:
                    flag = False
                    break
            if flag == False:
                result+=counter[i]
            else:
                return result
        
        return -1