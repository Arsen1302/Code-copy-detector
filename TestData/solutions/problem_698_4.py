class Solution:
    def solution_698_4(self, A: List[int]) -> List[bool]:
        # time O(n)
        # space O(1)
        output = []
        last_bit = 0
        for i in range(len(A)):
            new_bit = last_bit*2 + A[i]
            output.append(new_bit % 5 == 0)
            last_bit = new_bit
        return output