class Solution:
    def solution_505_2(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        cur = head
        res = 0
        connected = False
        
        while cur:
            if cur.val in nums:
                if not connected:
                    res += 1
                    connected = True
            else:
                connected = False
            cur = cur.next
            
        return(res)