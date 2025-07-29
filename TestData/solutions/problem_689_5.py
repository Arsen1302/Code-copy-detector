class Solution:
    def solution_689_5(self, n: int) -> int:
        binary=bin(n).replace("0b","")
        ones="1"*len(binary)
        binary,ones=int(binary,2),int(ones,2)
        return binary^ones