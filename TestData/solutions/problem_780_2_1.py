class Solution:
    def solution_780_2_1(self, queries: List[str], words: List[str]) -> List[int]:
        def solution_780_2_2(x):
            return x.count(min(x))

        ans = []
        
        for i in queries:
            count = 0
            for j in words:
                if(solution_780_2_2(i) < solution_780_2_2(j)):
                    count += 1
            
            ans.append(count)
        
        return ans