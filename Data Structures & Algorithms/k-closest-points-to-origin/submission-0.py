import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # quick sort based on dsa course for quick sort
        def dis(point: List[int]) -> float:
            return math.sqrt(point[0] ** 2 + point[1] ** 2)
        def quickSort(points: List[List[int]], s: int, e: int) -> None:
            if (e - s + 1) <= 1:
                return

            left = s
            pivot = points[e]

            for i in range(s, e):
                if dis(points[i]) < dis(pivot):
                    temp = points[left]
                    points[left] = points[i]
                    points[i] = temp
                    left += 1
            points[e] = points[left] # swap left and pivot elements to put pivot in the middle
            points[left] = pivot

            quickSort(points, s, left - 1)
            quickSort(points, left + 1, e)


        quickSort(points, 0, len(points) - 1)
        return points[:k]

    

