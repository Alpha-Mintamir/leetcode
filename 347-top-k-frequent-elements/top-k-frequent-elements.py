class Solution(object):
    def topKFrequent(self, nums, k):
        # Dictionary to store the frequency of each number
        frequency_dict = {}
        # List to store the final result
        result = []
        
        # Count the frequency of each number
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        # Sort the dictionary by frequency in descending order
        sorted_frequency = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)
        
        # Extract the top k elements
        for i in range(k):
            result.append(sorted_frequency[i][0])
        
        return result