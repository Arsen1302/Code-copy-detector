class Solution:
    def solution_659_2_1(self, arr: List[int]) -> int:
        def solution_659_2_2(odd, prev, curr):
			return curr < prev if odd else curr > prev
        
        n = len(arr)
        ans = 1
        for flip in [False, True]:
            l = 0
            for r in range(1, n):
                odd = r &amp; 1
                prev = arr[r-1]
                curr = arr[r]
                if flip: odd = not odd
                if not solution_659_2_2(odd, prev, curr): l = r
                ans = max(ans, r-l+1)
        
        return ans