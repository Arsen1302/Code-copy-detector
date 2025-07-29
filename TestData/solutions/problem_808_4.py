class Solution:
    def solution_808_4(self, nums: List[int]) -> int:
        ans = most = 0
        cnt = defaultdict(int)
        freq = defaultdict(int)
        for i, x in enumerate(nums):
            cnt[x] += 1
            freq[cnt[x]-1] -= 1
            freq[cnt[x]] += 1
            most = max(most, cnt[x])
            if most == 1 or most * freq[most] == i or (most-1)*freq[most-1] + most == i+1: ans = i+1
        return ans