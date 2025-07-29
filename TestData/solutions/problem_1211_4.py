class Solution:
    def solution_1211_4(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                # new_s = s[i:j+1]
                # count = Counter(new_s)
                count[s[j]] = count.get(s[j], 0) + 1
                if len(count.values()) > 1:
                    max_ = max(count.values())
                    min_ = min(count.values())
                    res += max_-min_
        return res