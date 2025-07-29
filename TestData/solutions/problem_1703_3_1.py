class Solution:
    def solution_1703_3_1(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def solution_1703_3_2(a, b):
            d = 0
            for i, j in zip(a, b):
                if i != j:
                    d += 1
                    if d > 2:
                        return False 
            return True 
        ans = []
        for q in queries:
            if any(solution_1703_3_2(q, d) for d in dictionary):
                ans.append(q)
        return ans