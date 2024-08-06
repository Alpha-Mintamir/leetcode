class Solution(object):
    def defangIPaddr(self, address):
        result = []
        address = address.split('.')
        return '[.]'.join(address)
        