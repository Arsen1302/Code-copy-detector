class Solution(object):
    def solution_126_1(self, s, memo=dict()):
        if s in memo:
            return memo[s]
        if s.isdigit(): # base case
            return [int(s)]
        calculate = {'*': lambda x, y: x * y,
                     '+': lambda x, y: x + y,
                     '-': lambda x, y: x - y
                    }
        result = []
        for i, c in enumerate(s):
            if c in '+-*':
                left = self.solution_126_1(s[:i], memo)
                right = self.solution_126_1(s[i+1:], memo)
                for l in left:
                    for r in right:
                        result.append(calculate[c](l, r))
        memo[s] = result
        return result