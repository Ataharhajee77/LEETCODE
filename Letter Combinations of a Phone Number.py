class Solution:
    def rec(self,digits):
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',                    '8': 'tuv', '9': 'wxyz'}
        
        if len(digits)==0:
            return ''
        
        if len(digits)==1:
            return phone[digits]
    
        front = phone[digits[0]]
        back = self.rec(digits[1:])
        res = [f+b for f in front for b in back ]
        
        return res
    def letterCombinations(self, digits: str) -> List[str]:
        return self.rec(digits)
