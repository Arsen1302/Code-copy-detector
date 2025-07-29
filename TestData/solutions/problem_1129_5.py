class Solution:
    def solution_1129_5(self, accounts: List[List[int]]) -> int:
        arr = []
        for i in range(len(accounts)):
            wealth = 0
            for j in accounts[i]:
                wealth += j
                arr.append(wealth)
        return max(arr)