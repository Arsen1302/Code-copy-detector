class Solution:
    def solution_758_2(self, hours: List[int]) -> int:
        n = len(hours)
        ans = 0
        prefix_sum = [0]*n
        d = {}
        for i in range(n):
            prefix_sum[i] = 1 if hours[i] > 8 else -1
            prefix_sum[i] += prefix_sum[i-1]
            if prefix_sum[i] > 0 : 
                ans = i + 1
            else:
                if prefix_sum[i] - 1 in d:
                    j = d[prefix_sum[i] - 1]
                    if i - j > ans: ans = i - j
            if prefix_sum[i] not in d: d[prefix_sum[i]] = i
        return ans