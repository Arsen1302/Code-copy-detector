class Solution:
    def solution_755_5(self, seq: str) -> List[int]:
        A = []
        B = []
        ans = []
        for i in seq:
            if i == '(':
                if A == [] and B == []:
                    A.append(i)
                    ans.append(0)
                elif len(A) < len(B):
                    A.append(i)
                    ans.append(0)
                else:
                    B.append(i)
                    ans.append(1)
            elif i == ')':
                if A and A[-1] == '(':
                    A.pop()
                    ans.append(0)
                elif B and B[-1] == '(':
                    B.pop()
                    ans.append(1)
        return ans