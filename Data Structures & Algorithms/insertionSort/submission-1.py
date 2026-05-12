# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        res = [pairs[:]]
        for i in range (1, len(pairs)):
            j = i - 1
            # print(f'j: {j}, {pairs[j+1].key}, {pairs[j].key}')
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                # print('bf swp')
                # print(f'{pairs[j].key}, {pairs[j+1].key}')
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1]
                # print('af swp')
                # print(f'{pairs[j].key}, {pairs[j+1].key}')
                j -= 1
            res.append(pairs[:])
        return res