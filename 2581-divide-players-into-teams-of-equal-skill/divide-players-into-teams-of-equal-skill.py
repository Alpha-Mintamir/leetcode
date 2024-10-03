
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        first_team = skill[left] + skill[right]
        result = 0
        
        while left < right:
            current_sum = skill[left] + skill[right]
            if current_sum != first_team:
                return -1
            result += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return result