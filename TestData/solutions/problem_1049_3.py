class Solution:
    def solution_1049_3(self, n: int) -> str:
        return re.sub('(?<=\d)(?=(\d{3})+$)', '.', str(n))