class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        area = 0
        stack = [] # track the starting index of the very last left bar higher than the bar and the exact height of a bar
        # so we can calculate the widest area where it can act as the shortest bar.
        for i, h in enumerate(heights):
            start = i
            # the highest bar in the stack cannot extend further to the right,
            # so we pop it and calculate area
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # current i - index gives us the best width possible for the bar in the stack
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        # calculate the remaining bars in the stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea