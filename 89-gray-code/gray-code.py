class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]
        visited = set([0])

        def generateGrayCode(num):
            if len(result) == 2 ** n:
                return True
            for i in range(n):
                next_num = num ^ (1 << i)

                if next_num not in visited:
                    result.append(next_num)
                    visited.add(next_num)

                    if generateGrayCode(next_num):
                        return True

                    result.pop()
                    visited.remove(next_num)
            return False

        generateGrayCode(0)
        return result