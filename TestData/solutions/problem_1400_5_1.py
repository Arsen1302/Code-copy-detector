class Solution:
    def solution_1400_5_1(self):
        base = ['1', '22', '333', '4444', '55555', '666666']
        nums = set()
        for comb in itertools.product([0,1], repeat=6):              # 64 combinations
            cur = ''
            for i, val in enumerate(comb):
                cur += base[i] if val else ''
            if len(cur) > 7:                                         # max `n` is 10^6, which is 7 digits
                continue 
            if cur:                                                  # permute all valid combinations
                nums |= set(itertools.permutations(cur, len(cur)))   # about 10^4
        nums = sorted([int(''.join(num)) for num in nums|set(base)]) # convert tuple to integer and sort           
        self.nums = nums
    def solution_1400_5_2(self, n: int) -> int:
        idx = bisect.bisect_right(self.nums, n)                      # binary search
        return self.nums[idx]                                        # return answer