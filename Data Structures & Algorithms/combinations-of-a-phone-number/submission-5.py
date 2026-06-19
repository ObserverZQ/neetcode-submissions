class Solution:
    # use combination O(k * C(n, k)) to solve this problem.
    # here we use index i to get every digit rather than a simple number-like i,
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        num_chac = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        def helper(curStr, index):
            if len(curStr) == len(digits) and curStr:
                res.append(curStr)
                return
            if index >= len(digits):
                return
            for j in range(index, len(digits)):
                chacs = num_chac[int(digits[j])]
                for c in chacs:
                    curStr += c
                    helper(curStr, j + 1)
                    curStr = curStr[:-1]

        helper('', 0)
        return res