class Solution:
    def solution_812_2(self, s: str) -> int:
        # take window sum of all 4 ?
        # instead of window sum, 
        # should we maintain remaining sum!
        # fre of elements outside the window ;)
        
        # initially window is empty..
        remaining_fre = collections.Counter(s)
        res = n = len(s)
        left = 0
        for right, c in enumerate(s):
            remaining_fre[c] -= 1
            
            # while window is valid that is:
            # remaining does not have any EXTRA elements!!
            # EXTRA element is any (element > n/4)
            while left < n and all(remaining_fre[ch] <= n/4 for ch in 'QWER'):
                
                res = min(res, right-left+1)
                remaining_fre[s[left]] += 1 # he goes out of window! into remaining
                left += 1
                
        return res
    
"""

WHILE LEFT < N 


while loop condition is most trick!!! :
https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/408978/JavaC%2B%2BPython-Sliding-Window

Important
Does i <= j + 1 makes more sense than i <= n.
Strongly don't think, and i <= j + 1 makes no sense.

Answer the question first:
Why do we need such a condition in sliding window problem?

Actually, we never need this condition in sliding window solution
(Check all my other solutions link at the bottom).

Usually count the element inside sliding window,
and i won't be bigger than j because nothing left in the window.
"""