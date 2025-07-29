class Solution:
    def solution_513_3(self, ages):
        count = [0] * 121                               # counter: count frequency of each age
        for age in ages:
            count[age] += 1
        prefix = [0] * 121                              # prefix-sum: prefix sum of frequency, we will use this for range subtraction
        for i in range(1, 121):
            prefix[i] = prefix[i-1] + count[i]
        nums = [i for i in range(121)]                  # a dummy age list, which will be used in binary search
        ans = 0
        for age, cnt in enumerate(count):
            if not cnt: continue
            lb = age                                    # lower bound
            ub = (age - 7) * 2                          # upper bound
            i = bisect.bisect_left(nums, lb)            # binary search on lower bound, O(log(121))
            j = bisect.bisect_left(nums, ub)            # binary search on upper bound, O(log(121))
            if j - i <= 0: continue
            total = prefix[j-1] - prefix[i-1]           # range subtraction - how many ages in total can be considered as friend, including current age itself
            if lb <= age < ub:                          # considering itself, e.g. [17, 17, 17]
                # total -= cnt                          # minus itself
                # total = (cnt - 1) * cnt + total * cnt # make friends with other at same age `(cnt-1) * cnt`; with other at different age `total * cnt`
                total = cnt * (total - 1)               # a cleaner presentation of above two lines
            ans += total    
        return ans