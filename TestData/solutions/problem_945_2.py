class Solution:
    def solution_945_2(self, k: int) -> int:
        l=[1,1]
        a=0

        while l[len(l)-1] <= k:
            a += l[len(l)-1]+l[len(l)-2]
            if a > k:
                break
            l.append(a)
            a=0
        b = l[::-1]
        ans = 0
        for i in b:
            if i<=k:
                ans = ans + 1
                k -= i
            if k == 0:
                break
        return ans