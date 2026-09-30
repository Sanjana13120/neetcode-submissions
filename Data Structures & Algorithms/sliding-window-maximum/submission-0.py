class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        res = []

        for i in range(len(nums)):
            while q and q[0] < i - k + 1:
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])

        return res


"""
TC: O(n)
SC: O(k)

goal - Return a list that contains the maximum element in the window at each step.

approach:

1. Remove expired index from FRONT.
2. Remove smaller values from BACK.
3. Add current index.
4. If window size >= k → answer = value at FRONT.

Input: nums = [1,2,1,0,4,2,6], k = 3

1 2 1 0 4 2 6
            i

i=0 q=[0]
i=1 
    nums[q[-1]]<nums[1] = 1<2? yes so q=[1]

i=2 
    nums[q[-1]]<nums[2] = 2<1? no q=[1,2]

i==k-1? yes

res=[2] append q[0]

i=3
    1<0? no q=[1,2,3]
    res=[2,2]

i=4 
    0<4? yes q=[1,2]
    1<4? yes q=[1]
    2<4? yes q=[]

    q=[4]
    i>=k-1? res=[2,2,4]

i=5
    4<2? no q=[4,5]
    i>=k-1? res=[2,2,4,4]

i=6
    2<6? yes q=[4]
    4<6? yes q=[]

    q=[6]
    i>=k-1? res=[2,2,4,4,6]





"""
