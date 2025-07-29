class Solution:
    def solution_1645_3(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = collections.Counter()
        for st, e, right in shifts:
            d[st] += 1 if right else -1         # Mark at the beginning to indicate everything after it need to be shifted
            if e+1 < n:                         # Mark (inversely) at the index after the end, to negate the unnecessary shifts
                d[e+1] += -1 if right else 1
        prefix = [0]                            # Initialize the prefix array
        ans = ''
        for i in range(n):                      # Use prefix sum style to accumulate all shifts needed, which were carried over from the previous index
            cur = prefix[-1] + d[i]
            prefix.append(cur)
            ans += string.ascii_lowercase[(ord(s[i]) - ord('a') + cur) % 26]
        return ans