class Solution:
    def solution_1607_2(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        x, y, dx, dy = 0, 0, 1, 0
        for i in range(len(matrix) * len(matrix[0])):
            if i > len(lst) - 1:
                break
            matrix[y][x] = lst[i]

            if not 0 <= x + dx < n:
                dx, dy = -dy, dx
            elif not 0 <= y + dy < m:
                dx, dy = -dy, dx
            elif matrix[y + dy][x + dx] != -1:
                dx, dy = -dy, dx

            x, y = x + dx, y + dy
        return matrix