class Solution:
    def solution_471_5(self, answers):
        count_dict = Counter(answers)
        ans = 0
        for n, c in count_dict.items():
            if c % (n+1) == 0:
                group = (c // (n+1))
            else:
                group = (c // (n+1)) + 1

            ans += (n+1) * group
        return ans