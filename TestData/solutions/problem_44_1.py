class Solution(object):
    @cache  # the memory trick can save some time
    def solution_44_1(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.solution_44_1(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans