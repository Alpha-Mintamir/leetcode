class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        distances = [0] * n

        prefixCount = 0
        prefixSum = 0

        for i in range(n):
            distances[i] = prefixCount * i - prefixSum
            if boxes[i] == '1':
                prefixCount += 1
                prefixSum += i

        suffixCount = 0
        suffixSum = 0

        for i in range(n - 1, -1, -1):
            distances[i] += suffixSum - suffixCount * i
            if boxes[i] == '1':
                suffixCount += 1
                suffixSum += i

        return distances