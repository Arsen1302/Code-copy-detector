class Solution:
    def solution_664_5(self, a: int, b: int) -> str:
		# n = current # of consecutive chracters in res that are the same
		# positive if it's consecutive as, negative if it's bs
        n = 0
        res = ''
        while a and b:
            if n == -2 or (n != 2 and a >= b):
                res += 'a'
                a -= 1
                n = max(1, n + 1)
            else:
                res += 'b'
                b -= 1
                n = min(-1, n - 1)
        return res + (a * 'a') + (b * 'b')