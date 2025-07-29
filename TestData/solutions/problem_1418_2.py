class Solution:
    def solution_1418_2(self, tickets: List[int], k: int) -> int:
        return sum(min(x, tickets[k] if i <= k else tickets[k] - 1) for i, x in enumerate(tickets))