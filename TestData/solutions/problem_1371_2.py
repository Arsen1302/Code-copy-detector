class Solution:
    def solution_1371_2(self, changed: List[int]) -> List[int]:
        changed.sort()
        stk,res=deque([]),[]
        for i in changed:
            if stk and stk[0]*2==i:
                b=stk.popleft()
                res.append(b)
            else:
                stk.append(i)
        return res if not stk else []