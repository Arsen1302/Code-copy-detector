class Solution:
    def solution_1247_4(self, costs: List[int], coins: int) -> int:
        costs.sort()
        l = [costs[0]]
        c = costs[0]
        for i in range(1,len(costs)):
            c += costs[i]
            l.append(c)
        return len([i for i in l if i <= coins])