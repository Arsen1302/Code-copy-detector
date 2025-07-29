class Solution:
    def solution_945_5(self, k: int) -> int:
        coins=[]
        coins.append(1)
        coins.append(1)


        while(coins[-1]<=k):
            coins.append(coins[-1]+coins[-2])

        coins=coins[::-1]


        rem=k
        total_coins=0
        for i in range(0,len(coins)):
            if(coins[i]>rem):
                continue
            elif(rem==0):
                break
            else:

                total_coins+=int(rem/coins[i])
                rem=rem%coins[i]

        return(total_coins)