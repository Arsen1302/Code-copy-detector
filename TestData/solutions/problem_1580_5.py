class Solution:
    def solution_1580_5(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        calc_price = lambda cost, discount: cost * (discount / 100)

        for i, w in enumerate(words):
            if w.startswith("$"):
                price = w[1:]
                if price and "$" not in price and price.isdigit():
                    words[i] = f'${int(price) - calc_price(int(price), discount):.2f}'

        return " ".join(words)