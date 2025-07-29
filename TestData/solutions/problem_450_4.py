class Solution:
    def solution_450_4(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" not in deadends: 
            ans = 0
            queue = ["0000"]
            deadends.add("0000")
            while queue: 
                newq = []
                for n in queue: 
                    if n == target: return ans 
                    for i in range(4): 
                        for chg in (-1, 1): 
                            nn = n[:i] + str((int(n[i]) + chg) % 10) + n[i+1:]
                            if nn not in deadends: 
                                newq.append(nn)
                                deadends.add(nn)
                queue = newq
                ans += 1
        return -1