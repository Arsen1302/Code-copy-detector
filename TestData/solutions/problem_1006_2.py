class Solution:
    def solution_1006_2(self, arr: List[int], k: int) -> bool:
        h = {}
        for i in arr:
            r = i % k
            if r not in h:
                h[r] = 0
            h[r]+=1

        if h.get(0,0) %2 !=0:
            return False

        for r1 in h:
            r2 = k - r1
            if r1 == 0:
                continue
            if h[r1] != h.get(r2,0):
                return False
        return True
# Please upvote if you understand the solution