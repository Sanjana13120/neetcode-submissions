class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = []

        for num in nums:

            if not temp or num > temp[-1]: 
                temp.append(num)
            else:
                start = 0
                end = len(temp)

                while start<end:
                    mid = start + (end-start)//2

                    if temp[mid]>=num:
                        end=mid

                    else:
                        start=mid+1

                temp[start]=num


        return len(temp)
          
    
'''
tc: O(logn)
sc: O(n)

optimal soln: Binary search
Input: nums = [9,1,4,2,3,3,7]

1. we will maintain an temp array that will be in sorted way
2. If curr is greater than the last element of temp, append it. 
   else,  find the first element in temp that is >= curr and replace it.

9 1 4 2 3 3 7
            i

temp = []

i=9 temp = [9]

i=1 1>9? no 
start=0 end=1 mid=0
9>=1?yes end=0 
so replace  temp= [1]

i=4 4>1> yes append temp= [1,4]

i=2 2>4 no  
start=0 end=2 mid=1 
4>=2? yes end=1 
0<1? mid=0
1>=2? no start=1 
so replace temp=[1,2]

i=3 3>2? yes append temp=[1,2,3]

i=3 3>3 no replace temp=[1,2,3]

i=7 7>3? yes append temp=[1,2,3,7]

--------------------------------------------------------------------------------------------

0 3 1 3 2 3
          i
i=0 temp=[0]

i=3 3>0? yes temp=[0,3]

i=1 1>3 no start=0 end=2 mid=1
3>=1? yes end=1 start=0 mid=0
0>=1? no start=1 end=1 1<1?no
temp=[0,1]

i=3 3>1?yes temp=[0,1,3]

i=2 2>3? no start=0 end=3 mid=1
1>=2? no start=2 end=3 mid=2
3>=2? yes end=2 start=2   2<2?no
temp=[0,1,2]

i=3 3>2? yes temp=[0,1,2,3]








'''