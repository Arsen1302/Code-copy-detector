class Solution:
    def solution_1580_3(self, sentence: str, discount: int) -> str:
        return re.sub(
            r"(?:(?<=\s)|(?<=^))\$\d+(?:(?=\s)|(?=$))",
            lambda x: "${:.2f}".format(float(x.group(0)[1:]) * (100 - discount) / 100),
            sentence,
        )