class Solution:
    def solution_1469_3(self, target: int, dob: int) -> int:
        if dob==0: return target-1
        ans=0
        while dob>0 and target>1:
            if target%2==0:
                target//=2
                dob-=1
            else:
                target-=1
                    
            ans+=1
        return ans+target-1