class Solution:
    def solution_1424_2_1(self, k: int, n: int) -> int:

        def solution_1424_2_2(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(n % b)
                n //= b
            return digits[::-1]
        
        # not used
        def solution_1424_2_3(arr, b):
            ans = 0
            for x in arr:
                ans = ans * b + int(x)
            return ans
        
        def solution_1424_2_4(s):
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def solution_1424_2_5():
            '''
            generate for value with different length
            when i == 0: num：[1, 10)
            size of num: 1, 2 -> 1 or 11
            when i == 1: [10, 100)
            size of num: 3, 4 -> 10 or 101
            when i == 2: [100, 1000)
            size of num: 5, 6 -> 10001 or 100001
            
            the num will be increasing
            '''
            for i in range(30):
                for num in range(10**i, 10**(i+1)):
                    s = str(num) + str(num)[::-1][1:]
                    yield int(s)
                for num in range(10**i, 10**(i+1)):
                    s = str(num) + str(num)[::-1]
                    yield int(s)
        
        ans = 0
        left = n
        for num in solution_1424_2_5():
            base = solution_1424_2_2(num, k)
			# if solution_1424_2_4(base):
            if base == base[::-1]:
                ans += num
                left -= 1
            if left == 0:
                break

        return ans