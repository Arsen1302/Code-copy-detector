class Solution:
    def solution_739_2(self, s: str) -> str:
        d = defaultdict(list)
        for index,character in enumerate(s):
            d[character].append(index)
        unique = sorted([ x for x in d])
        
        # what should be the character at index = 1
        size = len(unique)
        ans = ""
        used = {}
        left = 0
        for i in range(size):
            for character in unique:
                if character in used:continue
                if d[character][-1] < left: continue
                # find the new left
                idx = bisect.bisect_left(d[character],left)
                new_left = d[character][idx]
                # check if current character can be used
                flag = True
                for character2 in unique:
                    if character2 in used or character2 == character: continue
                    if d[character2][-1] < new_left:
                        flag = False
                        break
                if flag == True:
                    left = new_left
                    ans += character
                    used[character] = True
                    break
        return ans