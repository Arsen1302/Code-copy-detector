class Solution:
    def solution_505_1(self, head: ListNode, G: List[int]) -> int:
        Gs = set(G)
        ans = 0
        while head: 
            if head.val in Gs and (head.next is None or head.next.val not in Gs): ans += 1
            head = head.next 
        return ans