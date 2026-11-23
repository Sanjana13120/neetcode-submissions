class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n<=0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]!=1) and (i==len(flowerbed)-1 or flowerbed[i+1]!=1):
                flowerbed[i]=1
                n-=1

            if n==0:
                return True
        
        return False
        


'''
tc: O(n)
sc: O(1)


Approach: Greedy

- Traverse the flowerbed from left to right.
- If the current position is empty and both neighbours are empty (or the position is a boundary), plant a flower.
- Decrease n after planting.
- If n becomes 0, return True.
- If we finish traversal and n > 0, return False.

Edge cases:
- n == 0: No flowers need to be planted, return True.
- First index: No left neighbour to check.
- Last index: No right neighbour to check.
- Avoid planting adjacent flowers.

Input: flowerbed = [1,0,0,0,1], n = 1


1 0 1 0 1 

n=0

Input: flowerbed = [1,0,0,0,1], n = 2

1 0 1 0 1

n=1

'''