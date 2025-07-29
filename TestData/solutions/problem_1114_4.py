class Solution:
    def solution_1114_4(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        p = 0
        for i in range(10**5):
            if inventory[i]>inventory[i+1]:
                if (i+1)*(inventory[i]-inventory[i+1])>=orders:
                    left, right = inventory[i+1]+1, inventory[i]
                    while left<=right:
                        mid = (left+right)//2
                        numBalls = (inventory[i]-mid+1)*(i+1)
                        if 0<=numBalls-orders<i+1:
                            k = numBalls-orders
                            p += ((inventory[i]+mid)*(inventory[i]-mid+1)//2)*(i+1)-(k*mid)
                            return p%1000000007
                        elif numBalls<orders:
                            right = mid-1
                        else:
                            left = mid+1
                else:
                    orders -= (i+1)*(inventory[i]-inventory[i+1])
                    p += ((inventory[i]+inventory[i+1]+1)*(inventory[i]-inventory[i+1])//2)*(i+1)