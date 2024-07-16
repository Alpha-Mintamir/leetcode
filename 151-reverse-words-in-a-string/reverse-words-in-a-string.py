class Solution(object):
    def reverseWords(self, s):
        list1 = split(s)
        left, right = 0, len(list1)-1
        while left < right:
            list1[left], list1[right] = list1[right], list1[left]
            left += 1
            right -= 1
        s = " ".join(list1)
        return s
        