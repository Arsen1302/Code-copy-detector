class Solution:
    def solution_902_4(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        left  = set(x for x in leftChild  if x != -1)
        right = set(x for x in rightChild if x != -1)
        return len(left | right) == n-1 and (not left &amp; right)