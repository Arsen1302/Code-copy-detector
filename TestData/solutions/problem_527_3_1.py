class Solution:
    def solution_527_3_1(self, strs: List[str]) -> int:

        def solution_527_3_2(a, b):
            cnt = 0
            for a_, b_ in zip(a, b):
                if a_ != b_:
                    cnt += 1
            return cnt <= 2
        u = [i for i in range(len(strs))]

        def solution_527_3_3(i):
            parent = u[i]
            if parent == i:
                return i
            else:
                root = solution_527_3_3(parent)
                u[parent] = root
                return root
                
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                a_root = solution_527_3_3(i)
                b_root = solution_527_3_3(j)
                if a_root != b_root:
                    if solution_527_3_2(strs[i], strs[j]):
                        u[a_root] = b_root
        
        cnt = set()
        for i in range(len(strs)):
            cnt.add(solution_527_3_3(i))
        return len(cnt)