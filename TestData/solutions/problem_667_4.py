class Solution:
    def solution_667_4(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        q = [(root, 0)]
        start = end = 0
        while q :
            n = len(q)
            curr = defaultdict(list)
            for i in range(n) :
                temp = q.pop(0)
                start = min(start, temp[1])
                end = max(end, temp[1])
                curr[temp[1]].append(temp[0].val)
                if temp[0].left :
                    q.append((temp[0].left, temp[1]-1))
                if temp[0].right :
                    q.append((temp[0].right, temp[1]+1))
            for i in curr :
                d[i] += sorted(curr[i])
        return [d[i] for i in range(start, end+1)]