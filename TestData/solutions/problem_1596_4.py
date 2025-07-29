class Solution:
    def solution_1596_4(self, s: str, k: int) -> int:
        b = bin(k)[2:]
        print(b)
        ind = []
        for i in range(len(b)):
            if b[i] == '1':
                ind.append(len(b)-i-1)
        flag = True
        l = 0
        for i in s[::-1]:
            if i == '0':
                l += 1
            else:
                while ind and l > ind[-1]:
                    ind.pop()
                    flag = True
                if ind and ind[-1] == l and not flag:
                    ind.pop()
                if ind:
                    l += 1
                    flag = False
        return l