class Solution:
    def solution_1069_2(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        dd = {}
        
        for i,x in pairs:
            dd[i] = preferences[i][:preferences[i].index(x)]
            dd[x] = preferences[x][:preferences[x].index(i)]
        
        ans = 0
            
        for i in dd:
            for x in dd[i]:
                if i in dd[x]:
                    ans += 1
                    break
        
        return ans