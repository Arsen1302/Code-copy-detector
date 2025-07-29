class Solution:
    def solution_1476_3(self, nums: List[int]) -> int:
        nums.sort()
        freq_table = Counter(nums)
        arr = list(freq_table.keys())
        arr.sort()
        ans = len(nums)
        ans -= freq_table[arr[0]]
        ans -= freq_table[arr[-1]]
        return max(ans,0)