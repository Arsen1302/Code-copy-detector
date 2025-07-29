class Solution:
    def solution_1580_4_1(self, sentence: str, discount: int) -> str:
        """If you use regex, now you have two problems. 

        Lots of trial and error on regex101.com

        254 ms, faster than 40.17%
        """
        
        def solution_1580_4_2(m):
            rep = float(m.group(2)) * (100 - discount) / 100
            return f'${rep:.2f}'

        return re.sub(r'(^|(?<=\s))\$(\d+)(?=\s|$)', solution_1580_4_2, sentence)