class Solution:
    def solution_1327_4(self, s: str, k: int) -> int:
        nums = [str(ord(c) - ord('a') + 1) for c in s]
        nums = ''.join(nums)
        for i in range(k):
            nums = str(sum(map(int, nums)))
        return nums