class Solution:
    def solution_699_1_1(self, head: ListNode) -> List[int]:
        result = []
        stack = []
        for i, current in enumerate(self.solution_699_1_2(head)):
            result.append(0)
            while stack and stack[-1][0] < current:
                _, index = stack.pop()
                result[index] = current
            stack.append((current, i))
        return result

    def solution_699_1_2(self, head: ListNode):
        while head is not None:
            yield head.val
            head = head.next