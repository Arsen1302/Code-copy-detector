class Solution:
    def solution_12_4(self, num: int) -> str:
        mapping = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        arr = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        result = ""
        for a in arr:
            while num >= a:
                num = num - a
                result = result + mapping[a]
        return result