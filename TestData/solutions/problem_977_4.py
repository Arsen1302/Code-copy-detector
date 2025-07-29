class Solution:
    def solution_977_4(self, s: str, k: int) -> int:
        prefix_sum = []
        if s[0] in "aeiou":
            prefix_sum.append(1)
        else:
            prefix_sum.append(0)
        for i in range(1, len(s)):
            if s[i] in "aeiou":
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(prefix_sum[-1])
        result = prefix_sum[k - 1]
        for i in range(k, len(s)):
            result = max(result, prefix_sum[i] - prefix_sum[i - k])
        return result