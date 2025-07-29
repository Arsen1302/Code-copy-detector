class Solution:
    def solution_1408_2(self, head: Optional[ListNode]) -> List[int]:
        arr,dist=[],[]
        diff=10 ** 5 
        index=0
        while head:
            arr.append(head.val)
            head=head.next
        for i in range(1,len(arr)-1):
            if (arr[i-1] > arr[i] and arr[i+1] >arr[i]) or (arr[i-1] < arr[i] and arr[i]> arr[i+1]):
                dist.append(i)
                if index>=1:
                    diff=min(diff,dist[index]-dist[index-1])
                index+=1
        if not dist or len(dist)==1:return [-1,-1]
        else: 
            return [diff,dist[-1]-dist[0]]