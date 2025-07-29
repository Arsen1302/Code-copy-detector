class Solution:
    def solution_1557_5(self, number: str, digit: str) -> str:
        ans = []
        for ind,i in enumerate(number):
            if i == digit:
                ans.append(int(number[:ind]+number[ind+1:]))
        return str(max(ans))