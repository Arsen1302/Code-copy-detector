class Solution:
    def solution_946_4(self, n: int, k: int) -> str:
        total = 3 * 2 ** (n - 1)
        if k > total:
            return ""
        k -= 1
        ret = ""
        for i in range(n):
            if i:
                total //= 2
                d = k // total + ord("a")
                if d >= ord(ret[-1]):
                    d += 1
                ret += chr(d)
            else:
                total //= 3
                ret += chr(k // total + ord("a"))
            k %= total
        return ret