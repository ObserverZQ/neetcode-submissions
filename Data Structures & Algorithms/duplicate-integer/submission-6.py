class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # my first thought: use a set. time: O(n), space: O(n)
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False