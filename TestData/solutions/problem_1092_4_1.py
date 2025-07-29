class Solution:
    def solution_1092_4_1(self, a: str, b: str) -> bool:
        n=len(a)
        
        # Brute Force: TLE
        # for i in range(n):
        #     s1=a[:i]+b[i:]
        #     s2=b[:i]+a[i:]
        #     if s1==s1[::-1] or s2==s2[::-1]:
        #         return True
        # return False
        
        # 2 pointers
        def solution_1092_4_2(s1,s2):
            l=0
            r=n-1
            while l<=r and s1[l]==s2[r]:
                l+=1
                r-=1
            
            if l>r or s1[l:r+1]==s1[l:r+1][::-1] or s2[l:r+1]==s2[l:r+1][::-1]:
                return True
            return False
        return solution_1092_4_2(a,b) or solution_1092_4_2(b,a)