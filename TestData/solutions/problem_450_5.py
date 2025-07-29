class Solution:
    def solution_450_5(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" not in deadends: 
            deadends.add("0000")
            pq = [(0, "0000")]
            
            while pq: 
                k, n = heappop(pq)
                if n == target: return k 
                for i in range(4): 
                    for chg in (-1, 1): 
                        nn = n[:i] + str((int(n[i]) + chg) % 10) + n[i+1:]
                        if nn not in deadends: 
                            deadends.add(nn)
                            heappush(pq, (k+1, nn))
        return -1