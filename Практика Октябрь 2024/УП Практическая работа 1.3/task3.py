def max_area_in_file(input_file):
    with open(input_file, 'r') as f:
        heights = list(map(int, f.read().strip().split()))
    
    left = 0
    right = len(heights) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        current_height = min(heights[left], heights[right])
        current_area = width * current_height
        
        max_area = max(max_area, current_area)
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

input_file = 'nums.txt'

max_water_area = max_area_in_file(input_file)

print(f"Максимальная площадь воды: {max_water_area}")
