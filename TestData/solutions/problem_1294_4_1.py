class Solution:
    def solution_1294_4_1(self, s: str, p: str, removable: List[int]) -> int:
        # You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable.
    # as usual we can search through the answer.

        left = 0
        right = len(removable)
        lenS, lenP = len(s), len(p)
        def solution_1294_4_2(target):
            seen = set(removable[:target])
            if target == 0:
                return True
            sIndx,pIndx = 0, 0
            while sIndx < lenS and pIndx < lenP:
                if sIndx in seen:
                    pass
                elif s[sIndx] == p[pIndx]:
                    pIndx += 1
                sIndx += 1
            return pIndx == lenP


        while left <= right:
            mid = left + ((right-left)//2)
            if solution_1294_4_2(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right