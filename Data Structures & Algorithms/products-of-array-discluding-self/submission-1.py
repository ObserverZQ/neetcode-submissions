class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # to efficiently get the products,
        # we need to accumulate previous results, from left and right.
        # what about from left to right once and from right to left once?
        # i wanna use two arrays, each position records the accumulated result from one direction before itself.
        n = len(nums)
        ltor, rtol = [1] * n, [1] * n
        
        for i in range(n):
            if i == 0:
                continue
            else:
                # i >= 1, so we have the previous element's value and the previous index's accumulation
                ltor[i] = ltor[i - 1] * nums[i - 1]
        #         print('i', i)
        #         print('ltor[i]', ltor[i])
        # print('ltor', ltor)
        for i in range(n-1, -1, -1):
            if i == n - 1:
                continue
            else:
                # i >= 1, so we have the previous element's value and the previous index's accumulation
                rtol[i] = rtol[i + 1] * nums[i + 1]
        # print('ltor', ltor)
        # print('rtol', rtol)
        for i in range(n):
            ltor[i] = ltor[i] * rtol[i]
        return ltor
