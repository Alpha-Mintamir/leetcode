class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        common_elements = set()
        prefix_common_count = 0
        
        for i in range(len(A)):
            if A[i] == B[i]:
                prefix_common_count += 1
            else:
                if A[i] in common_elements:
                    prefix_common_count += 1
                if B[i] in common_elements:
                    prefix_common_count += 1
            
            common_elements.add(A[i])
            common_elements.add(B[i])
            
            result.append(prefix_common_count)
        
        return result