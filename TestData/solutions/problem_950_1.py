class Solution:
    def solution_950_1(self, croakOfFrogs: str) -> int:
        cnt, s = collections.defaultdict(int), 'croak'     
        ans, cur, d = 0, 0, {c:i for i, c in enumerate(s)}  # d: mapping for letter &amp; its index
        for letter in croakOfFrogs:                         # iterate over the string
            if letter not in s: return -1                   # if any letter other than "croak" is met, then invalid
            cnt[letter] += 1                                # increase cnt for letter
            if letter == 'c': cur += 1                      # 'c' is met, increase current ongoing croak `cur`
            elif cnt[s[d[letter]-1]] <= 0: return -1        # if previous character fall below to 0, return -1
            else: cnt[s[d[letter]-1]] -= 1                  # otherwise, decrease cnt for previous character
            ans = max(ans, cur)                             # update answer using `cur`
            if letter == 'k':                               # when 'k' is met, decrease cnt and cur
                cnt[letter] -= 1
                cur -= 1
        return ans if not cur else -1                       # return ans if current ongoing "croak" is 0