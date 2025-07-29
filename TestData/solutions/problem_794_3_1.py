class Solution:
    def solution_794_3_1(self, n: int, a: int, b: int, c: int) -> int:
        a,b,c = sorted((a,b,c))
        ans = inf
        def solution_794_3_2(a,b):
            if a %b == 0: return b
            return solution_794_3_2(b , a % b)
        p,q,r= solution_794_3_2(a,b),solution_794_3_2(b,c),solution_794_3_2(a,c)
        s = solution_794_3_2(r,b)
        x1 = (a*b) // p
        x2 = (b*c) // q 
        x3 = (a*c) // r
        x4 = (a * b * c * s)// (p * q * r )
        low,high = a , a *n
        while low <= high:
            mid = (low + high)//2
            times = mid//a + mid//b + mid//c - mid//x1 - mid//x2 - mid//x3 + mid//x4
            if times < n : low = mid + 1
            elif times == n:
                ans = min(ans,mid)
                high = mid - 1
            else: high = mid - 1
        return ans