class Solution:
    def solution_642_4(self, nums: List[int]) -> int:
        
        dic = {}
        for i in nums :
            if i in dic :
                dic[i] += 1
                if dic[i] == len(nums)/2 :
                    return i
            else :
                dic[i] = 1