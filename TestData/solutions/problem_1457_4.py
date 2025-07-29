class Solution:
    def solution_1457_4(self, bank: List[str]) -> int:
        pre = 0
        nn = 0
        ans = 0
        for i in bank:
            nn= 0
            for j in i:
                if j == '1':
                    nn+=1
            if nn:
                ans+=nn*pre
                pre= nn
        return ans
## PLease upvote if you like the Solution