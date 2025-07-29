class Solution:
    def solution_1029_4(self, s: str, indices: List[int]) -> str:
        ans = ""  # taking empty string to save result
        for i in range(len(indices)): # loop for traversing
            ans += s[indices.index(i)] # firstly we`ll get the index of "i", and then we use that to have the char in the string. I.E. indices.index(0) = 4 ,s[4] = L
        return ans # giving out the answer.