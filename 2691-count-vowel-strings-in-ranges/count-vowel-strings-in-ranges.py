class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Use a set for faster lookup
        prefix_sum = [0]  # Prefix sum array to preprocess counts

        # Precompute the prefix sum array
        for word in words:
            is_vowel_string = word[0] in vowels and word[-1] in vowels
            prefix_sum.append(prefix_sum[-1] + (1 if is_vowel_string else 0))

        result = []
        for li, ri in queries:
            result.append(prefix_sum[ri + 1] - prefix_sum[li])

        return result
