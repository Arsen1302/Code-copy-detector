class Solution:
    def solution_530_5_1(self, num: str) -> List[int]:
        two_31 = 2 ** 31
        n = len(num)
        def solution_530_5_2(a, b, j):
            nonlocal n
            cur = []
            while j < n:
                a, b = b, a+b
                if b > two_31: return []
                b_str = str(b)
                if num[j:].startswith(b_str):
                    cur.append(b)
                    j += len(b_str)
                else:
                    return []
            else:
                return cur
            
        for i in range(1, n):
            if i > 1 and num[0] == '0': break
            a_str = num[:i]
            a = int(num[:i])
            if a > two_31: break
            for j in range(i+1, n):
                if j > i+1 and num[i] == '0': break
                b_str = num[i:j]
                b = int(num[i:j])
                if b > two_31: break
                cur = solution_530_5_2(a, b, j)
                if not cur: continue
                return [a, b] + cur
        return []