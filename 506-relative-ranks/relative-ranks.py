class Solution:
    def findRelativeRanks(self, score):
        # Create a dictionary to store the rank based on the sorted score
        medals_list = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_dict = {}

        # Sort the score list in descending order and enumerate over it
        sorted_score = sorted(score, reverse=True)
        for i, s in enumerate(sorted_score):
            if i < 3:  # Assign medals for the top 3
                rank_dict[s] = medals_list[i]
            else:  # Assign numeric ranks for the rest
                rank_dict[s] = str(i + 1)

        # Generate the result list based on the original score order
        result = [rank_dict[s] for s in score]
        return result
