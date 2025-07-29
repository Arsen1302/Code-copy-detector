class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def solution_1675_2(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]