class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # my idea: add parent for each person's list in a map
        # pop the person out of another list if it is in the trust 2-d list's 0th position
        # check the list len, only return the 0th person if len is 1
        trust_map = defaultdict(list)
        trust_count = defaultdict(int) # record how many ppl trust each person
        judges = {i: True for i in range(1, n+1)}
        for [a, b] in trust:
            # for [a, b] in pair:
            trust_map[a].append(b)
            trust_count[b] += 1
            judges.pop(a, None) # delete the person safely
        if len(judges) != 1:
            return -1
        candidate = list(judges.keys())[0]
        if trust_count[candidate] == n - 1:
            return candidate
        return -1