class Solution:
    def solution_275_3(self, n: int) -> int:
        if n in [1,2,3]:
            return 1
        s, p1, p2, curr, count = '122', 2, 3, '1', 1
        while p2 < n:
            s += curr * int(s[p1])
            p2 += int(s[p1])
            if curr == '1':
                if p2 > n:
                    count += p2 - n 
                    return count
                count += int(s[p1])
            curr = '1' if curr == '2' else '2'
            p1 += 1
        return count