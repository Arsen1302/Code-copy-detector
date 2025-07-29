class Solution:
    def solution_1166_1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = head  # left node
        for _ in range(k-1):
            l = l.next
        # the rest of the code logic here