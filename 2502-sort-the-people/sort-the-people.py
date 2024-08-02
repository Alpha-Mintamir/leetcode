class Solution(object):
    def sortPeople(self, names, heights):
        dictt = {}
        result = []
        for people, height in zip(names, heights):
            dictt[height] = people
        sorted_item = sorted(dictt.items(), key=lambda item: item[0], reverse=True)
        for item in sorted_item:
            result.append(item[1])
        return result