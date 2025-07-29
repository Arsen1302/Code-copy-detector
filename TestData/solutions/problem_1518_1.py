class Solution:

    def solution_1518_1(self, nums: List[int]) -> bool:
        lena = len(nums)
        count = sum(num//2 for num in Counter(nums).values())
        return (lena/2 == count)