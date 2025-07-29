class Solution:
    def solution_390_4(self, n: int, k: int) -> List[int]:
        ans = [1]
        num = k + 1
        flag = True
        diff = k
        while len(ans) < num:
            if flag:
                ans.append(ans[-1] + diff)
            else:
                ans.append(ans[-1] - diff)

            diff -= 1
            flag = not flag
        
        cur_max = num
        while len(ans) < n:
            end = ans[-1]
            for z in range(min(end + k, n), cur_max, -1):
                ans.append(z)
            cur_max = end + k
        
        return ans