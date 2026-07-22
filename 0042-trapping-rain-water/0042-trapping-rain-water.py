class Solution:
    def trap(self, height: List[int]) -> int:
        # find the summit index - index of highest elevation item  
        max_value = 0
        summit_index = -1
        for i in range(len(height)):
            if height[i] >= max_value:
                max_value = height[i]
                summit_index = i 

        # define our algorithm
        def algo(ls):
            water = 0
            current_max_height = 0
            for i in ls: # i is current_wall_size
                if i > current_max_height:
                    current_max_height = i
                elif i < current_max_height:
                    water += current_max_height-i
            return water

        # run our algorithm
        total_water = 0
        total_water += algo(height[:summit_index])
        total_water += algo(reversed(height[summit_index+1:]))
        return total_water