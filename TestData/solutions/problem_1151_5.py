class Solution:
    def solution_1151_5(self, binary: str) -> str:
        return '1'*binary.find('0')+reduce(lambda a,b:a+b if b=='1' else a[:-1]+'10', sorted(binary[max(binary.find('0'),0):]))