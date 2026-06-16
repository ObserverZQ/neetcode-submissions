class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        left = right = n
        def backtrack(l, r, cur):
            if l == 0 and r == 0:
                res.append(cur)
                return
            
            if l == 0:
                cur += ')'
                backtrack(l, r - 1, cur)
                return
            
            # a str with more ( to be appended cannot be valid.
            if r < l:
                return

            cur += '('
            backtrack(l - 1, r, cur)
            cur = cur[:len(cur) - 1]
            cur += ')'
            backtrack(l, r - 1, cur)
        backtrack(n, n, '')
        return res