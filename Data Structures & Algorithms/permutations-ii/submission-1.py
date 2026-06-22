class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms = [[]]

        for n in nums:
            nextPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    nextPerms.append(pCopy)
                    # we detect that the current n is the same as the a num in the perm which occurs for the first time, so we stop putting num in other pos as that would result in duplicate perms
                    if i < len(p) and n == p[i]:
                        break
                    
            perms = nextPerms

        return perms