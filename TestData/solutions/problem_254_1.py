class Solution:
    def solution_254_1(self, g: List[int], s: List[int]) -> int:
        g.sort()  # O(nlogn)
        s.sort()  # O(nlogn)
        
        child_point = 0
        cookie_point = 0
        counter = 0
        
        # O(n)
        while child_point < len(g) and cookie_point < len(s):
            if g[child_point] <= s[cookie_point]:
                counter += 1
                child_point += 1
                cookie_point += 1
            else:
                cookie_point += 1
            
        return counter