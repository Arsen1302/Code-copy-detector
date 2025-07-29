class Solution:
    def solution_1607_5(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        n,m=m,n
        arr=[[-1]*m for i in range(n)]
        r,c=0,0
        
        while True:
            j=c
            # first row
            while head and j<m:
                arr[r][j]=head.val
                head=head.next
                j+=1
            i=r+1
            # last column
            while head and i<n:
                arr[i][m-1]=head.val
                head=head.next
                i+=1
            j=m-2
            # last row
            while head and j>=c:
                arr[n-1][j]=head.val
                head=head.next
                j-=1
            i=n-2
            # first column
            while head and i>r:
                arr[i][c]=head.val
                head=head.next
                i-=1
            # check if there's still data in linked list
            if not head:
                break
            r+=1
            c+=1
            m-=1
            n-=1
        return arr