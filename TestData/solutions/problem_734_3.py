class Solution:
    def solution_734_3(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # find the sum of both binary number in decimal form
        ans = 0
        start = 1
        for i in arr1[::-1]:
            if i == 1:ans += start
            start *= -2
        start = 1
        for i in arr2[::-1]:
            if i == 1:ans += start
            start *= -2
        res = []
        # convert decimal to negative 2 base
        while ans:
            rem = ans % -2
            ans = ans // -2
            if rem < 0: ans += 1
            res.append(abs(rem))
        res = res[::-1]
   ``     return res if res != [] else [0]