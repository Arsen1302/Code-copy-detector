class Solution:
    def solution_1623_3(self, rolls: List[int], k: int) -> int:

        z = set()
        res = 0

        for x in rolls:
            z.add(x)
            if len(z) == k:
                res += 1
                z.clear()
                
        return res + 1