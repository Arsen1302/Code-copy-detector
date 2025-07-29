class Solution:
    def solution_699_5(self, head: ListNode) -> List[int]:
        values = []
        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next
        ans = [0]*len(values)
        stack = []
        for i,j in enumerate(values):
            if not stack or stack[-1][0] > j:
                stack.append((j,i))
            else:
                while stack and stack[-1][0] < j:
                    ans[stack.pop()[1]] = j
                stack.append((j,i))
        return ans