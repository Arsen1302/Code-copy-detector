class Solution:
    def solution_1092_5_1(self, a: str, b: str) -> bool:
        def solution_1092_5_2(s1,s2):
            l,r = 0,len(s1)-1
            while l <= r and s1[l] == s2[r]:
                l += 1
                r -= 1
            #Return True if s1 and s2 is proven to form a palidrome (l > r) midway
            #If s1 and s2 do not form a palidrome midway, return True if one of s1 or s2
            #form a palidrome between index l and r 
            if l > r or s1[l:r+1] == s1[l:r+1][::-1] or s2[l:r+1] == s2[l:r+1][::-1]:
                return True
            return False
        
        return solution_1092_5_2(a,b) or solution_1092_5_2(b,a)