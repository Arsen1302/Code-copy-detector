class Solution:
    def solution_1518_3(self, nums: List[int]) -> bool:
        not_a_pair = set()
        
        for x in nums:
            if x not in not_a_pair:
                not_a_pair.add(x)
            else:
                not_a_pair.remove(x)
        return not not_a_pair