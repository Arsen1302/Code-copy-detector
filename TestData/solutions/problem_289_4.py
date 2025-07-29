class Solution:
    def solution_289_4(self, words: List[str]) -> List[str]:
        l = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []
        for i in words:
            a = i.lower()
            if len(set(a).difference(set(l[0]))) == 0 or len(set(a).difference(set(l[1]))) == 0 or len(set(a).difference(set(l[2]))) == 0:
                ans.append(i)
        return ans