class Solution:
    def solution_1452_3(self, num: int) -> bool:
        if num==0:return True
        string=str(num)
        rev="".join(list("".join(list(string)[::-1]).lstrip("0"))[::-1])
        return True if string==rev else False