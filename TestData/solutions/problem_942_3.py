class Solution:
    def solution_942_3(self, text: str) -> str:
        m = {
            '&amp;quot;': '\"',
            '&amp;apos;': "'",
            '&amp;amp;': '&amp;',
            '&amp;gt;': '>',
            '&amp;lt;': '<',
            '&amp;frasl;': '/'
        }
        
        delimiter = '$!@#$%^&amp;$'
        
        for k, v in m.items():
            text = text.replace(k, v+delimiter)
        
        return text.replace(delimiter, '')