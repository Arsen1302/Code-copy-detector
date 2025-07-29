class Solution:
    def solution_808_1(self, nums: List[int]) -> int:
        cnt, freq, maxfreq, ans = collections.defaultdict(int), collections.defaultdict(int), 0, 0
        for i, num in enumerate(nums):
            cnt[num] = cnt.get(num, 0) + 1
            freq[cnt[num]] += 1
            freq[cnt[num]-1] -= 1
            maxfreq = max(maxfreq, cnt[num])
            if maxfreq == 1:
                ans = i+1
            elif maxfreq*freq[maxfreq] == i:
                ans = i+1
            elif (maxfreq-1)*(freq[maxfreq-1]+1) == i:
                ans = i+1
        return ans