class Solution:
    def solution_1623_2(self, rolls: List[int], k: int) -> int:
        s = set()
        res = 0
        
        for r in rolls:
            s.add(r)
            if len(s) == k:        # All possible number has appeared once.
                res += 1           # So you must "at least" use one more place to store it.
                s.clear()          # Clear the set.
        
        
        return res + 1