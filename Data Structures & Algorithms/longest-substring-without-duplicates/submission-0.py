class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # my thought: traverse the entire string, 
        # runtime: O(n * m), space: O(m) to record unique characters
        # if len(s) <= 1:
            # return len(s)
        # unique_chac = set()
        # count = 0
        # maxCount = 0
        # i, j = 0, 0

        # while i < len(s):
        #     if s[i] not in unique_chac:
        #         if not unique_chac:
        #             # here we record the starting index of the subtring being checked
        #             j = i
        #         unique_chac.add(s[i])
        #         count += 1
        #         i += 1
        #     else:
        #         # meet a repetitive character in the substring
        #         unique_chac.clear()
        #         count = 0
        #         # continue
        #         i = j + 1 # restore i to the starting point's next index 
        #     if count > maxCount:
        #         maxCount = count

        # return maxCount

        # 2. using a dynamic sliding window so that each character is added/removed at most once:
        # charSet = set()
        # left, right = 0, 0
        # count = 0
        # for right in range(len(s)):
        #     while s[right] in charSet:
        #         charSet.remove(s[left])
        #         left += 1
        #     charSet.add(s[right])
        #     count = max(count, right - left + 1)
        # return count

        # 3. move the left pointer immediately to the next position of the first position the character that gets repetitive, using a map that record each unique character's first appearance(index)
        uniqueMap = {}
        left, right = 0, 0
        count = 0
        for right in range(len(s)):
            if s[right] in uniqueMap:
                left = max(uniqueMap[s[right]] + 1, left) # make sure left can't move backward
            uniqueMap[s[right]] = right
            count = max(count, right - left + 1)
        return count