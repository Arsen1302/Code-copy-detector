class Solution:
    def solution_942_1(self, text: str) -> str:
        
        html_symbol = [ '&amp;quot;', '&amp;apos;', '&amp;gt;', '&amp;lt;', '&amp;frasl;', '&amp;amp;']
        formal_symbol = [ '"', "'", '>', '<', '/', '&amp;']
                
        for html_sym, formal_sym in zip(html_symbol, formal_symbol):
            text = text.replace( html_sym , formal_sym )
        
        return text