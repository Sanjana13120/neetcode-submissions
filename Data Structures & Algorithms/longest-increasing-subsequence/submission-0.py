class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)

        return max(dp)       

'''
tc: O(n**2)
sc: O(n)

goal - find the length of longest increasing subsequence

we can delete some or no ele without changing the order

nums = [9,1,4,2,3,3,7]

9 --> >9 x (lenght=1)
1--> (>1) --> 4 --> 7  --- [1,4,7]  (lenght=3)
1--> 2-->3 --> 7 ---[1,2,3,7]  (lenght=4)
4--> 7 ---[4,7]      (lenght=2)
2-->3-->7 [2,3,7]    (lenght=3)
3-->7 ---[3,7]       (lenght=2)

longest = 4

approach: dp? coz we either have to delete or dont delete the ele (take or dont take)

base: dp = [1,1,1,1,1]

states: dp[i] = longest increasing subsequence ending at nums[i]

transition: dp[i]= max(dp[i],dp[j]+1)  where j<i and nums[j]<nums[i]


nums = [9,1,4,2,3,3,7]

9 1 4 2 3 3 7
          i
dp = [1,1,1,1,1,1,1,1]

i=1 j=0 --> 9<1? x

i=2 j=0 --> 9<4? x

i=2 j=1 --> 1<4? yes
    dp[2] = max(1,2)=2
    dp = [1,1,2,1,1,1,1]

i=3 j=0 --> 9<2? x

i=3 j=1--> 1<2? yes
    dp[3]= max(1,2)=2
    dp = [1,1,2,2,1,1,1]

i=3 j=2 -- 4<2? x

i=4 j=0 -- 9<3?x

i=4 j=1 -- 1<3? 
    dp[4]= max(1,2)=2
    dp = [1,1,2,2,2,1,1]

i=4 j=2 --> 4<3? x

i=4 j=3 -->2<3?yes
    dp[4] =max(2,3)=3
    dp = [1, 1, 2, 2, 3, 1, 1]

i=5 j=0 --9<3? x

i=5 j=1--> 1<3? yes
    dp[5]=max(1,2)=2
    dp = [1, 1, 2, 2, 3, 2, 1]

i=5 j=2 -->4<3?no

i=5 j=3 -->2<3?yes
    dp[5]= max(2,3)=3  dp = [1, 1, 2, 2, 3, 3, 1]

i=5 j=4 --> 3<3? no

i=6 j=0--> 9<7? x

i=6 j=1 -- 1<7?yes
    dp[6]=max(1,2)=2  dp = [1, 1, 2, 2, 3, 3, 2]

i=6 j=2 --> 4<7? yes
    dp[6]=max(2,3)=3  dp = [1, 1, 2, 2, 3, 3, 3]

i=6 j=3 -->2<7? yes
    dp[6]=max(3,3)=3  dp = [1, 1, 2, 2, 3, 3, 3]

i=6 j=4 --> 3<7? yes
    dp[6]=max(3,4)=4  dp = [1, 1, 2, 2, 3, 3, 4]

i=6 j=5 -> 3<7? yes
    dp[6]=max(4,4)=4  dp = [1, 1, 2, 2, 3, 3, 4]

return dp[n-1]=4

'''