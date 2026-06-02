class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # pick: indicator of whether an element at index i has been chosen or not
        def add(perm: List[int], pick: List[bool]) -> List[int]:
            if len(perm) == len(nums):
                # print(f'perm: {perm}')
                res.append(perm[:]) # we got 1,2,3 then backtrack to 1,2 then back to 1
                return
            for i in range(len(nums)):
                # start from the first element, we keep exploring in function stacks
                # we got: 1, 2, 3. then back to 1,2 then 1
                # then we increment i to the 2nd pos, which is 3, and get 1,3, then 1,3,2
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    add(perm, pick)
                    perm.pop()
                    pick[i] = False
        add([], [False] * len(nums))
        return res