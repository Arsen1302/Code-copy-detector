class Solution:
    def solution_590_4(self, left: str, right: str) -> int:
        left,right = int(left),int(right)
        limit = 100000
        count = 0
        for i in range(limit):
            s = str(i)
            # 121 -> 12121 and 121121
            s1 = s + s[::-1][1:]
            s2 = s + s[::-1]
            tmp1,tmp2 = pow(int(s1),2),pow(int(s2),2)
            if (tmp1 > right):
                break
            if str(tmp1) == str(tmp1)[::-1] and int(tmp1) >= left:
                count += 1
            if str(tmp2) == str(tmp2)[::-1] and tmp1 != tmp2 and int(tmp2) <= right and int(tmp2) >= left:
                count += 1
        return count