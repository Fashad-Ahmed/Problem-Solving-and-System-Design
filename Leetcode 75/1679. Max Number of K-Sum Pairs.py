class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq_map = {}
        operations = 0
        
        for num in nums:
            complement = k - num
            
            # If the complement exists and is available, we have a pair
            if freq_map.get(complement, 0) > 0:
                operations += 1
                freq_map[complement] -= 1
            else:
                # Otherwise, add the current number to the map for future pairs
                freq_map[num] = freq_map.get(num, 0) + 1
                
        return operations
