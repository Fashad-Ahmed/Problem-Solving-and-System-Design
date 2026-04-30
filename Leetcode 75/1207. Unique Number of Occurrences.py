class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        values = list(freq.values())

        return len(values) == len(set(values))
