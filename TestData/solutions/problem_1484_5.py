class Solution:
    def solution_1484_5(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        greater = []
        for num in nums:
            if (num < pivot):
                lesser.append(num)
            elif num > pivot:
                greater.append(num)
        return lesser + ([pivot] * nums.count(pivot)) + greater