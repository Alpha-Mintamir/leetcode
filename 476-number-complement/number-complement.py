class Solution:
    def findComplement(self, num: int) -> int:
        
        binary_num = bin(num)[2:] 
        complement = ''
        for bit in binary_num:
            
            if bit == '1':
                complement += '0'
            else:
                complement += '1'
        return int(complement, 2)
