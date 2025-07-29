class Solution:
    def solution_1607_3(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        id, jd, ret, i, j, i_min, i_max, j_min, j_max  = 0, 1, [[-1 for j in range(n)] for i in range(m)], 0, 0, 0, m-1, 0, n-1

        while head is not None:

            ret[i][j] = head.val
            head=head.next

            if not (i_min <= i + id <= i_max and j_min <= j + jd <= j_max):
                id, jd = jd, -id
                i_min, i_max, j_min, j_max = i_min + max(0, id), i_max + min(0, id), j_min + max(0, jd), j_max + min(0, jd)

            i, j = i + id, j + jd

        return ret