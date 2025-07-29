class Solution:
    def solution_1549_4(self, nums: List[List[int]]) -> List[int]:
        return sorted(reduce(lambda x,y: set(x) &amp; set(y), nums))