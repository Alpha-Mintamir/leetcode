class Solution:
    def findRelativeRanks(self, score):
        medals_list = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_dict = {}

        sorted_score = sorted(score, reverse=True)
        for i, s in enumerate(sorted_score):
            if i < 3:  
                rank_dict[s] = medals_list[i]
            else:  
                rank_dict[s] = str(i + 1)


        result = [rank_dict[s] for s in score]
        return result
