class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a','i','o','u', 'e']
        half = int(len(s)/2)
        count_first = 0
        count_second = 0
        first_half = s[:half].lower()
        second_half = s[half:].lower()

        for i in first_half:
            if i in vowels:
                count_first +=1
        for i in second_half:
            if i in vowels:
                count_second +=1
        if count_first == count_second:
            return True
        else:
            return False
        
        