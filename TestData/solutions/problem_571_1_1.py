class Solution:
    def solution_571_1_1(self, A: str, B: str) -> List[str]:
        uncommon = []
        
        def solution_571_1_2(s , t):
            ans = []
            for i in s:
                if(s.count(i) == 1 and i not in t):
                    ans.append(i)
            
            return ans
        
        return solution_571_1_2(A.split() , B.split()) + solution_571_1_2(B.split() , A.split())