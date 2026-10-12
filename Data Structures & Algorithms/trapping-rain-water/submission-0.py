class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftmax = height[left]
        rightmax = height[right]

        maxamount = 0

        while left <= right:
            if leftmax <= rightmax:
                leftmax = max(leftmax, height[left])
                maxamount += leftmax - height[left]
                left += 1

            else:
                rightmax = max(rightmax, height[right])
                maxamount += rightmax - height[right]
                right -= 1

        return maxamount


"""
tc: O(n)
sc: O(1)

goal - Return the total amount of water that can be trapped between the bars.

approach: 2 pointers

Key Observation:
water trapped at index i = min(maxLeft, maxRight) - height[i]

where, 
maxLeft = tallest wall to the left of i
maxRight = tallest wall to the right of i

Why Two Pointers Work:

If leftMax <= rightMax:

    water level on the left side is determined by leftMax.
    Even if there are taller walls on the right, the left side is the limiting wall.
    So we can safely calculate: leftMax - height[left]
    and move left.

Else:
    rightMax is the limiting wall.
    So we can safely calculate: rightMax - height[right]
    and move right.

Input: height = [0,2,0,3,1,0,1,3,2,1]

0 1 2 3 4 5 6 7 8 9
0 2 0 3 1 0 1 3 2 1
            lr

left = 0
right = 9
leftMax = 0
rightMax = 1
maxamount=0

0<9? yes so leftmax=0 height[left]=0
maxamount= 0-0=0
left=1

left=1 right=9
1<9? 0<1? yes leftmax=max(0,2)=2 
maxamount=2-2=0
left+=1

left=2 right=9 leftmax=2 rightmax=1
2<1? no rightmax=max(1,1)=1
maxamount=0+1-1=0
right-=1

left=2 right=8 leftmax=2 rightmax=1
2<1? no rightmax=max(1,2)=2
maxamount=0+2-2=0
right=7

left=2 right=7 leftmax=2 rightmax=2
2<=2? leftmax=max(2,0)=2
maxamount=0+2-0=2
left+=1

left=3 right=7 leftmax=2 rightmax=2
2<=2? leftmax=max(2,3)=3
maxamount=2+3-3=2
left+=1

left=4 right=7 leftmax=3 rightmax=2
3<2? rightmax=max(2,3)=3
maxamount=2+3-3=2
right-=1

left=4 right=6 leftmax=3 rightmaz=3
3<=3? leftmax=max(3,1)=3
maxamount=2+3-1=4
left+=1

left=5 right=6 leftmax=3 rightmax=3
3<=3? leftmax=max(3,0)=3
maxamunt=4+3-0=7
left+=1

left=6 right=6 leftmax=3 rightmax=3
3<=3? leftmax=max(3,1)=3
maxamunt=7+3-1=9
left+=1

left=7 right=6

return maxamount=9




"""
