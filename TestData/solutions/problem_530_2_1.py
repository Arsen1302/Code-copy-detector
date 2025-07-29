class Solution:
    def solution_530_2_1(self, num: str) -> List[int]:
        def solution_530_2_2(i, ans):
            if i>=len(num):
                return len(ans)>2           
            n = 0
            for j in range(i, len(num)):
                n = n*10 + int(num[j]) 
                if len(ans)<2 or (ans[-1]+ans[-2]==n):
                    ans.append(n)
                    if solution_530_2_2(j+1, ans):
                        return True
                    ans.pop()
                if i==j and num[j]=='0': 
                    return False
        
        return solution_530_2_2(0, [])