class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        result = set()  
        s1 = s1.split()
        s2 = s2.split()
        
        count_s1 = {}
        count_s2 = {}
        
        for word in s1:
            if word in count_s1:
                count_s1[word] += 1
            else:
                count_s1[word] = 1
        
        for word in s2:
            if word in count_s2:
                count_s2[word] += 1
            else:
                count_s2[word] = 1
        

        for word in s1:
            if word not in s2 and count_s1[word] == 1:
                result.add(word)
        

        for word in s2:
            if word not in s1 and count_s2[word] == 1:
                result.add(word)
        
        return list(result)