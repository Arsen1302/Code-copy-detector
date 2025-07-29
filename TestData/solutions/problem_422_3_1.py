class Solution:
    def solution_422_3_1(self, s1: str, s2: str) -> int:
        
        def solution_422_3_2(s):
            return sum(map(lambda x: ord(x), list(s)))

        @functools.lru_cache(None)
        def solution_422_3_3(s1, s2):
            if not s1 and not s2:
                return 0
            if not s1:
                return solution_422_3_2(s2)
            
            if not s2: 
                return solution_422_3_2(s1)


            ans = float("inf")

            if s1[0] == s2[0]:
                ans = min(ans, solution_422_3_3(s1[1:], s2[1:]))
            
            ans = min(ans, ord(s2[0]) + solution_422_3_3(s1, s2[1:]),  ord(s1[0]) + solution_422_3_3(s1[1:], s2),  ord(s1[0]) + ord(s2[0]) + solution_422_3_3(s1[1:], s2[1:]))

            return ans

        return solution_422_3_3(s1, s2)