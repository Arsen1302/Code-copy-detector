class Solution:
    def solution_1451_4(self, left: int, right: int) -> str:
        product=1
        for i in range(left,right+1):
            product *= i
        if(len(str(product).rstrip("0"))<=10):
            return str(product).rstrip("0") + "e" + str(len(str(product)) - len(str(product).rstrip("0")))
        else:
            return str(product).rstrip("0")[:5] +"..."+ str(product).rstrip("0")[-5:]+"e" + str(len(str(product)) - len(str(product).rstrip("0")))