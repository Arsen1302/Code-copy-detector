class Solution:
    def solution_1598_3(self, s: str) -> int:
        l = []
        temp = ''
        for i in s:
            if i == '|':
                temp += i
                # reset the temp, if a pair is closed
                if temp.count('|') == 2:
                    temp = ''
            # ignore the characters in between a pair
            if '|' in temp:
                continue
            # if none of the above conditions are met append the character into the list
            elif i != '|':
                l.append(i)
        return ''.join(l).count('*')