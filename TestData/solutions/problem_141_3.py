class Solution:
    def solution_141_3(self, nums: List[int]) -> int:
        # Use concept of 142. Linked List Cycle II (find the node where linked list has cycle)
        
        # start hopping from Node
        slow, fast = 0, 0
        # Cycle detection
        # Let slow jumper and fast jumper meet somewhere in the cycle 
        while True:
            # slow jumper hops 1 step, while fast jumper hops two steps forward.
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # for locating start node of cycle
        check = 0
        while True:
            # Locate the start node of cycle (i.e., the duplicate number)
            slow = nums[slow]
            check = nums[check]
            
            if check == slow:
                break
        
        return check