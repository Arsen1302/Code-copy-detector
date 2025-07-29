class Solution:
    def solution_425_5(self, bits: List[int]) -> bool:
        return '1' not in ''.join([str(bit) for bit in bits[:-1]]).replace('11', '').replace('10', '')