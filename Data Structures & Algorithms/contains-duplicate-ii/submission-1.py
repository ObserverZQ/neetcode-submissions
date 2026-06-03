class Solution:
    # sliding window + hashset. time: O(n), space: O(min(n, k))
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        visited = set([nums[l]])
        for r in range(1, len(nums)):
            # print(f'visited: {visited}, l: {l}, r: {r}')
            if (r - l) > k:
                visited.remove(nums[l])
                l += 1
            if nums[r] in visited:
                return True
            else:
                visited.add(nums[r])
        return False