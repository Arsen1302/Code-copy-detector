class Solution:
    def solution_1177_5(self, time: str) -> str:
        hr,mn = time.split(':')
        hr = list(hr)
        mn = list(mn)
        if hr[0]=='?' and hr[1]!='?':
            if 4<= int(hr[1]) <=9:
                hr[0] = "1"
            else:
                hr[0] = "2"
        if hr[1]=='?' and hr[0]!='?':
            if hr[0] == "2":
                hr[1] = "3"
            else:
                hr[1] = "9"
                
        if hr[0]=='?' and hr[1]=='?':
            hr[0] = "2"
            hr[1] = "3"
        
        if mn[0] == '?' and mn[1]!='?':
            mn[0] = "5"
        if mn[1] == '?' and mn[0]!='?':
            mn[1] = "9"
        if mn[0] == '?' and mn[1]=='?':
            mn[0] = "5"
            mn[1] = "9"
        hr.append(':')
        return "".join(hr+mn)