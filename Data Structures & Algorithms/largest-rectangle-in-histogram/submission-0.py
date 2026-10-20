class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                area = heights[idx] * width
                maxarea = max(maxarea, area)
            stack.append(i)

        while stack:
            idx = stack.pop()
            width = len(heights) - stack[-1] - 1 if stack else len(heights)
            area = heights[idx] * width
            maxarea = max(maxarea, area)

        return maxarea


"""
tc: O(n)
sc: O(n)

goal - Return the area of the largest rectangle

1. Approach
Use a monotonic increasing stack to store indices of bars.
Calculate rectangle areas when a shorter bar is encountered.
After the main loop, process any remaining indices because their rectangles may extend to the end of the histogram.

2. Intuition
For each bar, find the maximum width over which a rectangle of that bar's height can extend.

Right boundary: The first shorter bar to the right.
Left boundary: The nearest shorter bar to the left.
If no shorter bar exists on the left, the rectangle can start at index 0.
If no shorter bar exists on the right, the rectangle can extend to the last index.

Formula:

Area = height × width

When a bar is popped during the main loop:
If the stack is nonempty: width = i - stack[-1] - 1
If the stack is empty: width = i

When processing remaining bars after the main loop:
If the stack is nonempty: width = n - stack[-1] - 1
If the stack is empty: width = n
Here, n = len(heights).

3. Algorithm
Initialize an empty stack and maxarea = 0.
Iterate through each index i.
While the stack is nonempty and the current height is less than the height at the stack's top:
        Pop the index.
        Calculate the rectangle's width and area.
        Update maxarea.
Push the current index.
Process all remaining stack indices, using the end of the histogram as the right boundary.
Return maxarea.

4. Why are there two loops?
First loop: Calculates areas when a shorter bar establishes the right boundary.
Second loop: Handles bars that never encounter a shorter bar to their right.
Without the second loop, some maximum rectangle areas may never be calculated.


Input: heights = [7,1,7,2,2,4]

0 1 2 3 4 5
7 1 7 2 2 4
          i
stack = []

i=0
    stack = [0]
i=1
    1<7? so height 7 cannot be extended
    idx=0 stack = []
    height[0]=7
    width=1
    area=7
    stack = [1]

i=2
    7<1?no
    stack=[1,2]

i=3
    2<7? yes 
    idx=2 stack=[1]
    width=1
    height[2]=7
    area=7
    2<1? no
    stack=[1,3]

i=4 
    2<2? no
    stack = [1,3,4]

i=5
    4<2? no
    stack = [1,3,4,5]


stack = [1,3,4,5]
so process the indices remaining in the stack, because they may form larger rectangles.

pop 5
    idx=5
    height[5]=4
    stack=[1,3,4]
    width = len(heights)-idx-1 = 6-4-1=1
    area=max(7, 4*1)=7
    

pop 4
    idx=4
    heights[4]=2
    stack=[1,3]
    width = 6-3-1=2
    area=max(7,4)=7
    

pop 3
    idx=3
    height[3]=2
    stack=[1]
    width=6-1-1=4
    area=max(7,8)=8
    

pop 1
    idx =1
    height[1]=1
    stack = []
    width=6
    area=8

"""
