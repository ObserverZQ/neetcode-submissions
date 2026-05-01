class Solution:
    # time O(nlogn) space O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a tuple list with elements from two lists with corresponding indices
        # pair = 
        pair = list(zip(position, speed))
        # print(f'pair: {pair}')
        pair.sort(reverse = True) # sort the tuple list with the position in descending order
        # print(f'pair: {pair}')
        stack = []
        for p, s in pair:
            stack.append((target - p) / s) # the time it takes for the current car to reach the destination
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # the front car(-2) takes longer, so the later car catches up and merges with it
                stack.pop()
        return len(stack)
