class Solution:
    # two pointers. time O(n), space O(1)
    '''
    The height is limited by the shorter line, so to potentially increase the area, we must move the pointer at the shorter line inward.
    Moving the taller line never helps because it keeps the height(the height of the shorter bar) the same but reduces the width.
    By always moving the shorter side, we explore all meaningful possibilities(the width decreases but the shorter bar might be higher).
    '''
    def maxArea(self, heights: List[int]) -> int:
        # my thought: this question requires thinking about the index diff
        # as well as the lower bar's height among the two selected bars
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > maxArea:
                maxArea = area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea
            