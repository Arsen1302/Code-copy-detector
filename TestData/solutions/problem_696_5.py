class Solution:
    def solution_696_5(self, s: str, n: int) -> bool:
        leng_s = len(s)
        for i in range(1,n+1):
            binary = str(bin(i)[2:])
            leng_b = len(binary)
            flag = False
            for j in range(leng_s - leng_b + 1):
                if s[j:j + leng_b] == binary:
                    flag = True
                    break
            if flag == False:return False
        return True