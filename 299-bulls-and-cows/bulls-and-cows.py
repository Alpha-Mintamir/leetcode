class Solution(object):
    def getHint(self, secret, guess):
        countA = 0
        countB = 0
        secret_dict = {}
        guess_dict = {}
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                countA += 1
            else:
                secret_dict[secret[i]] = secret_dict.get(secret[i], 0) + 1
                guess_dict[guess[i]] = guess_dict.get(guess[i], 0) + 1
        

        for key in guess_dict:
            if key in secret_dict:
                countB += min(secret_dict[key], guess_dict[key])
        
        result = [str(countA), "A", str(countB), "B"]
        return ''.join(result)