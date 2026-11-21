class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x // 2

        if x<2:
            return x

        while start <= end:
            mid = start + (end - start) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                start = mid + 1
            else:
                end = mid - 1
            
        return end


"""
tc: O(logn)
sc: O(1)

goal -  return the square root of x rounded down to the nearest integer. 
Approach: Binary Search
x=9

start = 1 end   = 4
    mid   = 2
    sq    = 4<9? start=3

start=3 end=4 mid=3
    sq=9==9? return mid

----------------------------------

x=13

start=1 end=6 mid=3
    sq=9<13 start=4

start=4 end=6 mid=5
    sq=25>13 end=4

start=4 end=4 mid=4
    sq=16>13 end=3



"""
