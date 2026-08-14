class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=nums[0]

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]

            if slow==fast:
                break

        slow=nums[0]

        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return slow        


'''
tc: O(n)
sc: O(1)

### Floyd's cycle detection algorithm (Slow and fast pointer approach)###

Treat array as a linked list: index -> nums[index]

Duplicate creates a cycle.

Phase 1:
- slow moves 1 step
- fast moves 2 steps
- meet somewhere inside the cycle

Phase 2:
- reset slow to nums[0]
- move both 1 step
- find the cycle entrance
- cycle entrance = duplicate

--------------------------------------------------------------------------------------
0 1 2 3 4
1 2 3 2 2 
  s
      f

slow = 3
fast = 3

slow = nums[slow]
fast = nums[nums[fast]]

if slow==fast: break

slow = nums[0]=1
fast = 3

slow!=fast
slow=nums[slow] = 2
fast=nums[fast] = 2

return 2

--------------------------------------------------------------------------------------

1 2 3 4 4
      s 
        f

slow=4
fast=4

slow=1
fast=4

slow!=fast: 4!=4 false

slow=4
fast=4

return 4


--------------------------------------------------------------------------------------
hashmap (freq counting)
freq= {1:1 2:3 3:1} 
loop over freq and check count>1 return that num

tc: O(n)
sc: O(n)

'''