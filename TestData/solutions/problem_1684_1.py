class Solution:
    def solution_1684_1(self, num1: int, num2: int) -> int:       
        nbit1 = 0
        while num2>0:
            nbit1 = nbit1 + (num2&amp;1)
            num2 = num2 >> 1
        # print(nbit1)
        
        chk = []
        ans = 0
        # print(bin(num1), bin(ans))
        for i in range(31, -1, -1):
            biti = (num1>>i)&amp;1
            if biti==1 and nbit1>0:
                num1 = num1 &amp; ~(1<<i)
                ans = ans | (1<<i)
                chk.append(i)
                nbit1 -= 1
        # print(bin(num1), bin(ans))
        
        if nbit1>0:
            for i in range(0, 32, 1):
                biti = (num1>>i)&amp;1
                if i not in chk and nbit1>0:
                    num1 = num1 | (1<<i)
                    ans = ans | (1<<i)
                    nbit1 -= 1
        # print(bin(num1), bin(ans))
        # print("=" * 20)
        
        return ans