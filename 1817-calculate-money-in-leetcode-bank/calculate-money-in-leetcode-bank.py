class Solution:
    def totalMoney(self, n: int) -> int:
        total_sum = 0
        for week in range(n // 7):
            total_sum += sum(range(week + 1, week + 8))
       
        remaining_days = n % 7
        if remaining_days:
            total_sum += sum(range((n // 7) + 1, (n // 7) + 1 + remaining_days))
        
        return total_sum
