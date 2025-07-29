class Solution:
    def solution_1519_5(self, text: str, pattern: str) -> int:
        first=0
        second=0
        answer=0
        for i in text:
            if i==pattern[0]:
                first+=1
            if i==pattern[1]:
                second+=1
                if pattern[0]!=pattern[1]:
                    answer+=first
                else:
                    answer+=(first-1)
        return max(answer+second,answer+first)