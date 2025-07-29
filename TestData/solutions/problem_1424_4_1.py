class Solution:
    def solution_1424_4_1(self, k: int, n: int) -> int:
        def solution_1424_4_2(b: int):
            l = 1
            while True:
                for i in range(b ** ((l - 1) // 2), b ** ((l + 1) // 2)):
                    n = i
                    pal = i
                    if l % 2 == 1:
                        n //= b
                    while n:
                        pal = pal * b + (n % b)
                        n //= b
                    yield pal
                l += 1

        pk = solution_1424_4_2(k)
        p10 = solution_1424_4_2(10)

        numbers = []
        n10 = next(p10)
        nk = next(pk)

        while numbers.__len__() < n:
            if n10 == nk:
                numbers.append(n10)
            if n10 < nk:
                n10 = next(p10)
            else:
                nk = next(pk)
        return sum(numbers)