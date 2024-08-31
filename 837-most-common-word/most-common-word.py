class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph)
        words = paragraph.split()
        word_count = {}
        
        for word in words:
            if word not in banned:  
                word_count[word] = word_count.get(word, 0) + 1
        most_common_word = max(word_count, key=word_count.get)
        
        return most_common_word