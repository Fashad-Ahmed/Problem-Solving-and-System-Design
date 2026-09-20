def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # 1. Calculate the dimensions of the current container
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        # 2. Update the record if this container holds more water
        max_water = max(max_water, current_area)
        
        # 3. The crucial step: move the pointer of the shorter wall
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water
