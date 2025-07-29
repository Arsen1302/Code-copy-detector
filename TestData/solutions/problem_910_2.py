class Solution:
    def solution_910_2(self, s: str) -> int:
        d = collections.defaultdict(lambda: sys.maxsize)
        cur = (0, 0, 0, 0, 0)                            # current mask
        ans = d[cur] = -1                                # initialize result
        vowel = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4} # index mapping
        for i, c in enumerate(s):
            if c in vowel:                               # if `c` is a vowel, update the `cur` (mask)
                idx = vowel[c]
                cur = cur[:idx] + (1-cur[idx],) + cur[idx+1:]
            if d[cur] == sys.maxsize: 
                d[cur] = i                               # if mask is never recorded, recorded it since it's the lowest index of this current mask
            ans = max(ans, i - d[cur])                   # update `ans` by calculating `i - lower_idx_of_mask`
        return ans