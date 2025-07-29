class Solution:
    def solution_1723_3_1(self, root, queries):
        ans = []

        def solution_1723_3_2(node):
            if not node:
                return 

            solution_1723_3_2(node.left)
            ans.append(node.val)
            solution_1723_3_2(node.right)

        solution_1723_3_2(root)

        res = []

        n = len(ans)

        for i in queries:
            r1 = bisect.bisect_left(ans,i)

            if r1 == n: res.append([ans[-1],-1])
            elif ans[r1] == i: res.append([i,i])
            elif r1 == 0: res.append([-1,ans[0]])
            else: res.append([ans[r1-1],ans[r1]])

        return res