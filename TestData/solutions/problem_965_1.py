class Solution:
    def solution_965_1(self, arr: List[int]) -> int:
        import collections
        if len(arr) < 2:
            return 0
        xors = arr[0]
        cnt = collections.Counter()
        cnt_sums = collections.Counter()        
        result = 0
        cnt[xors] = 1
        cnt_sums[xors] = 0
        for k in range(1, len(arr)):
            xors ^= arr[k]
            if xors == 0:
                result += k
            result += (k - 1)*cnt[xors] - cnt_sums[xors]
            cnt_sums[xors] += k
            cnt[xors] += 1
            
        return result