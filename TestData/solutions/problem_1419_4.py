class Solution:
    def solution_1419_4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr, curr = [], head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next        
        i, counter = 0, 1
        arr2 = []
        while i < len(arr):
            if len(arr[i:i + counter]) % 2 == 0:
                arr2 += arr[i:i + counter][::-1]
            else:
                arr2 += arr[i:i + counter]
            i += counter
            counter += 1
            if i >= len(arr):
                break
        curr = head
        for item in arr2:
            curr.val = item
            curr = curr.next
        return head