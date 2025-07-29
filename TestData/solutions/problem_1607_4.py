class Solution:
    def solution_1607_4(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        left, right, top, bottom = 0, n-1, 0, m-1
        cur = head
        while cur:
		    # Go left -> right
            for c in range(left, right+1):
                if not cur: break
                matrix[top][c] = cur.val
                cur = cur.next
            
			# Go top right -> bottom right
            for r in range(top+1, bottom+1):
                if not cur: break
                matrix[r][right] = cur.val
                cur = cur.next
            
			# Go bottom right -> bottom left
            for c in range(right-1, left-1, -1):
                if not cur: break
                matrix[bottom][c] = cur.val
                cur = cur.next
            
			# Go bottom -> top 
            for r in range(bottom-1, top, -1):
                if not cur: break
                matrix[r][left] = cur.val
                cur = cur.next
            
			# Update boundary
            left += 1
            right -= 1
            top += 1
            bottom -= 1
            
        return matrix