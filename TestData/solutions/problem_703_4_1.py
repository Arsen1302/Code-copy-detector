class Solution:
    def solution_703_4_1(self, query, pattern):
        pidx = 0
        for i in range(len(query)):
            if query[i].isupper():
                if query[i]==pattern[pidx]:
                    pidx+=1
                else:
                    return False
            else:
                if query[i]==pattern[pidx]:
                    pidx+=1  
            if pidx==len(pattern):
                for j in range(i+1, len(query)):
                    if query[j].isupper():
                        return False
                return True

            
    def solution_703_4_2(self, queries: List[str], pattern: str) -> List[bool]:
        ans = [False for _ in range(len(queries))]
        for i in range(len(queries)):
            if self.solution_703_4_1(queries[i], pattern):
                ans[i]=True
        return ans