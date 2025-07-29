class Solution:
    def solution_269_4(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = k = 0 
        for x in sorted(houses):
            while k < len(heaters) and heaters[k] < x: k += 1
            cand = inf 
            if k < len(heaters): cand = min(cand, heaters[k] - x)
            if k: cand = min(cand, x - heaters[k-1])
            ans = max(ans, cand)
        return ans