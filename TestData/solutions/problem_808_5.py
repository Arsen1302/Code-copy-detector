class Solution:
    def solution_808_5(self, nums: List[int]) -> int:
        ans = 0
        cnt, freq = {}, {}
        for i, x in enumerate(nums): 
            if x in cnt and cnt[x] in freq: 
                freq[cnt[x]] -= 1
                if not freq[cnt[x]]: freq.pop(cnt[x])
            cnt[x] = 1 + cnt.get(x, 0)
            freq[cnt[x]] = 1 + freq.get(cnt[x], 0)
            if len(freq) == 1 and (1 in freq or 1 in freq.values()): ans = i+1
            elif len(freq) == 2 and (freq.get(1, 0) == 1 or freq.get(1+min(freq), 0) == 1): ans = i+1 
        return ans