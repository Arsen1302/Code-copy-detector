class Solution:
    def solution_450_3(self, deadends: List[str], target: str) -> int:
        ans = 0
        queue = ["0000"]
        deadends = set(deadends)
        while queue: 
            newq = []
            for n in queue: 
                if n not in deadends: 
                    deadends.add(n)
                    if n == target: return ans 
                    for i in range(4): 
                        for chg in (-1, 1): 
                            nn = n[:i] + str((int(n[i]) + chg) % 10) + n[i+1:]
                            newq.append(nn)
            queue = newq
            ans += 1
        return -1