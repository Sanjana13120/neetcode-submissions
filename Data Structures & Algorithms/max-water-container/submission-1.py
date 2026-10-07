class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        maxarea = 0

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maxarea = max(area, maxarea)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxarea


"""
tc: O(n)
sc :O(1)

goal - maximum amount of water a container can store.

Approach:
1. Initialize two pointers:
    left = 0
    right = len(height) - 1
2. Calculate the area formed by the two lines:
    area = width * height
    width = right - left
    height = min(height[left], height[right])
We use min() because the water level is limited by the shorter wall. Any water above the shorter wall would spill over.
3. Keep track of the maximum area seen so far.
4. Move the pointer at the shorter height:
    if height[left] <= height[right]:
        move left pointer
    else:
        move right pointer
Reason:
The shorter wall is currently limiting the container height. Moving the taller wall only decreases the width while keeping the same limitation. Moving the shorter wall gives us a chance to find a taller wall and potentially increase the area.

Input: height = [1,7,2,5,4,7,3,6]

0 1 2 3 4 5 6 7
1 7 2 5 4 7 3 6
    lr

left=0
right=7
area=0 

area = width * height
    width = right - left 
    height= min(height[left],height[right])

area= 7*1=7
maxarea= max(0,7)=7

1<6? left=1

left=1 right=7
area= 6* min(7,6)=6*6=36
maxarea=36

7>6 so right-=1

left=1 right=6
area=5*3=15
maxarea=36

7>3 right-=1

left=1 right=5
area=4*7=28
maxarea=36

7<=7 left+=1

left=2 right=5
area=3*2=6
maxarea=36

2<7 left+=1

left=3 right=5
area=2*2=4
maxarea=36

2<4 left+=1

left=4 right=5
area=1*2=2
maxarea=36

2<5 left+=1

left=5 right=5

so maxarea=36


"""
