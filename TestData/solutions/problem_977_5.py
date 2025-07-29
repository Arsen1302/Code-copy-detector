class Solution(object):
    def solution_977_5(self, s, k):
        ans = ptr = count = 0
        for i in range(len(s)):
            if k > i:
                if s[i] in 'aeiou': count += 1
                ans = count
            else:
                if s[ptr] in 'aeiou': count -= 1
                if s[i] in 'aeiou': count += 1
                if count > ans: ans = count
                ptr += 1
        return ans