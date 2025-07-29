class Solution:
    def solution_440_3(self, n: int) -> int:
        res = ""
        temp = str(n)[0]
        last = str(n)[0]
        d = len(str(n))
        k = 1
        for x in str(n)[1:]:
            if int(x)>int(temp):
                res += str(temp)*k
                k = 1
            elif int(x) == int(temp):
                k += 1
            else:
                last = str(temp)
                return int(res + str(int(last)-1) + "9"*(d-len(res)-1))

            temp = x

        
        return int(res+str(n)[-1]*k)