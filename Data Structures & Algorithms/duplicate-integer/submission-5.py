class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # my first thought: use a set
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False