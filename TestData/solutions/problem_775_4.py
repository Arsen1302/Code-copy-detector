class Solution:
    def solution_775_4(self, words: List[str], chars: str) -> int:
        output = 0
        for i in words:
            count = 0
            for j in i:
                if chars.count(j) >= i.count(j):
                    count+=1
                else:
                    break
            if count == len(i):
                output+=count
        return output