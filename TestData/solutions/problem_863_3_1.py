class Solution:
    def solution_863_3_1(self, s: str) -> int:
        @cache
        def solution_863_3_2(left,right):
            if left >= right:
                return 0

            # Characters are the same, move both both pointers inwards
            if s[left] == s[right]:
                return solution_863_3_2(left+1,right-1)
            
            # Add char at right pointer, since char added there to match left pointer, left+=1 (vice versa for tryRight)
            tryLeft = solution_863_3_2(left+1,right)
            tryRight = solution_863_3_2(left,right-1)

            # Return min of tryLeft and tryRight, +1 because you had to add a char on either the right or left side
            return min(tryLeft,tryRight)+1

        return solution_863_3_2(0,len(s)-1)