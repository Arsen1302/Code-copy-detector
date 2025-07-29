class Solution:
    def solution_95_5(self, head: ListNode) -> ListNode:
        #I will use the following head, prev, temp
        
        prev = None
        
        while head: #while head is present then this loop executes
            #first I will assign the value of head to the temp variable
            temp = head
            
            #now head can be pused to the next element
            head = head.next
            
            #now using temp in such a way to reverse the direction of the pointers
            temp.next = prev #this changes the current nodes pointer direction from right to left
            
            #now making prev come to the current node so that this same cycle can be repeated 
            prev = temp #this temp is the old value of temp that it carried before head gave and moved away
        return prev