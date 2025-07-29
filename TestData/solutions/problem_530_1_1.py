class Solution:
    def solution_530_1_1(self, num: str) -> List[int]:
        def solution_530_1_2(i):
            if i>=len(num):
                return len(ans)>2           
            n = 0
            for j in range(i, len(num)):
                n = n*10 + int(num[j]) 
                if n>2**31: # if number exceeds the range mentioned
                    return False
                # if len < 2 we know more elements need to be appended
                # as size>=3 if size is already greater we check for fibonacci
                # as last + secondLast == curr
                if len(ans)<2 or (ans[-1]+ans[-2]==n):
                    ans.append(n)
                    if solution_530_1_2(j+1):
                        return True
                    ans.pop()
                if i==j and num[j]=='0': # if trailing 0 is present
                    return False
        
        if len(num)<=2: return []
        ans = []
        if solution_530_1_2(0): return ans
        return []