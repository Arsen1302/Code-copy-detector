class Solution:
    def solution_2_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        _ = l1.val + l2.val
        digit, tenth = _ % 10, _ // 10
        answer = ListNode(digit)
        if any((l1.next, l2.next, tenth)):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += tenth
            answer.next = self.solution_2_2(l1, l2)    
        return answer