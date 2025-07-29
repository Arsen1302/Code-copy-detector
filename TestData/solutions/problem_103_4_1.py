class Solution:
    def solution_103_4_1(self, k: int, n: int) -> List[List[int]]:
        def solution_103_4_2(digit, start_num, cur, cur_sum):
            if cur_sum == n and digit == k: ans.append(cur[:])
            elif digit >= k or cur_sum > n: return    
            else:
                for i in range(start_num+1, 10):
                    cur.append(i)
                    solution_103_4_2(digit+1, i, cur, cur_sum+i)
                    cur.pop()
        ans = list()
        solution_103_4_2(0, 0, [], 0)
        return ans