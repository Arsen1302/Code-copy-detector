class Solution:
    def solution_1519_1(self, string: str, pattern: str) -> int:

        text = pattern[0]+string
        text1 = string + pattern[1]
        cnt,cnt1 = 0,0
        ans,ans1 = 0,0
        
        for i in range(len(text)):
            if text[i] == pattern[0]:
                cnt+=1
            elif text[i] == pattern[1]:
                ans+= cnt
        if pattern[0] == pattern[1]:
            ans = ((cnt)*(cnt-1))//2
        # appending at the last 
        for i in range(len(text1)):
            if text1[i] == pattern[0]:
                cnt1+=1
            elif text1[i] == pattern[1]:
                ans1+= cnt1
        if pattern[0] == pattern[1]:
            ans1 = ((cnt1)*(cnt1-1))//2
        return max(ans1,ans)