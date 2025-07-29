class Solution:
    def solution_494_3(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        pix_per_line = 0
        for i in s:
            if widths[ord(i) - 97] + pix_per_line <= 100:
                pix_per_line += widths[ord(i) - 97]
            else:
                lines += 1
                pix_per_line = widths[ord(i) - 97]
        return [lines, pix_per_line]