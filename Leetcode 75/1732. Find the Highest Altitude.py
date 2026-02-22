"""
gain[i]=altitude[i+1]-altitude[i]
Find max({altitude[i]})
"""
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0
        highest_altitude = 0
        for i in gain:
            current_altitude += i
            if (current_altitude > highest_altitude):
                highest_altitude = current_altitude
        return highest_altitude
        
