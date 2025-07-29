class Solution:
    def solution_1614_4(self, a: List[int]) -> int:
        result = 0
        

        while sum(a)!=0:
            result+=1
            a = sorted(a, reverse=True)
            if a[0] > 0:
                a[0] -= 1
                if a[1] > 0:
                    a[1] -=1
                elif a[2] > 0:
                    a[2] -= 1
        
        return result