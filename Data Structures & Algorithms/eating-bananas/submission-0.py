class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        while start < end:
            hours = 0
            mid = start + (end - start) // 2

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                end = mid
            else:
                start = mid + 1

        return start


"""
tc: O(nlog(max(piles)))
sc: O(1)

goal - find min rate at which all bananas can be eaten within h hours


approach: binary search
1. start=1 end=max(piles)
2. for each speed, calculate total hours
    For every pile:
       hours += ceiling(pile / mid)
Ceiling division:  (pile + mid - 1) // mid
3. compare total with h 
    if totalhours <= h: mid works
       → try a smaller speed
       → end = mid

   if totalhours > h:  mid is too slow
       → need a faster speed
       → start = mid + 1

5. Stop when:
   start == end

start is the minimum valid eating speed.
----------------------------------------------------
Input: piles = [1,4,3,2], h = 9

start = 1
end = 4
mid = 2

1//2 + 4//2 + 3//2 + 2//2 = 1+2+2+1=6
6<9 end=1 

stat=0 end=2

mid=1

1//1+ 4//1 + 3//1 + 2//1= 1+4+3+2=10>9 
so start=1 end =2

mid=1
1//1+ 4//1 + 3//1 + 2//1= 1+4+3+2=10>9 
start=2 end=2

return 2

----------------------------------------------------

Input: piles = [25,10,23,4], h = 4

start=1 
end=25
mid= 13

25//13 + 10//13 + 23//13 + 4//13 = 2+1+2+1= 6>4
so start=14

start=14 end=25 mid=19

25//19 + 10//19 + 23//19 + 4//19 = 2+1+2+1=6>4 
so start=20

start=20 end=25 mid=22

25//22 + 10//22 + 23//22 + 4//22 = 2+1+2+1 = 6>4 

start=23 end=25 mid=24
25//24 + 10//24 + 23//24 + 4//24 = 2+1+1+1=5>4

start=25 end=25 

return 25





"""
