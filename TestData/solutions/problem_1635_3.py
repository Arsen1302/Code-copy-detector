class Solution:
    def solution_1635_3(self, nums: List[int], diff: int) -> int:
        dic = {} # store nums[i]
        quest = {} # store require number you possible find after nums[i]
        count = 0 # count answer
        for i in nums:
            dic[i] = True 
            if i in quest: count += 1 # meet damand 
            if i - diff in dic: quest[i + diff] = True
        return count