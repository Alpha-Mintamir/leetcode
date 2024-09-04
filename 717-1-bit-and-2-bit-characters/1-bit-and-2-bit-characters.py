class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        a=0
        while a<len(bits):
            if bits[a]==1:
                a+=2
            else:
                if a==len(bits)-1:
                    return True
                else:
                    a+=1
        return False