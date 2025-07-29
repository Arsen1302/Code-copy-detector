class Solution:
    def solution_1062_1(self, s: str) -> int:
        total = s.count('1')
        if total % 3: return 0
        n = len(s)
        if not total: return (1+n-2) * (n-2) // 2 % 1000000007
        avg, ans = total // 3, 0
        cnt = first_part_right_zeros = last_part_left_zeros = 0
        for i in range(n):
            if s[i] == '1': cnt += 1
            elif cnt == avg: first_part_right_zeros += 1
            elif cnt > avg: break    
        cnt = 0
        for i in range(n-1, -1, -1):
            if s[i] == '1': cnt += 1
            elif cnt == avg: last_part_left_zeros += 1
            elif cnt > avg: break    
        return (first_part_right_zeros+1) * (last_part_left_zeros+1) % 1000000007