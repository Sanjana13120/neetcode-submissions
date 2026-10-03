class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        freq = {}

        for num in nums2:
            while stack and stack[-1] < num:
                freq[stack.pop()] = num

            stack.append(num)

        while stack:
            freq[stack.pop()] = -1

        return [freq[x] for x in nums1]

"""
tc: O(n + m), where n = len(nums2) and m = len(nums1)
sc: O(n)

goal - find the next greater ele of nums2[j] for j = values from nums1


Input: nums1 = [4,1,2], nums2 = [1,3,4,2]

num1=4 so we have to check the next greater ele of 4 in num2 --> no ele -1
num1=1 check the next greater ele of 1 in num2 --> 3
num1=2 next greater ele of 2 in num2 no ele so -1

approach: monotonic stack               


1. loop over each ele in num2 and append to stack
2. if stack[-1]<num then freq[stack[-1]]:num
3. now loop over nums1 and look in freq


num=1 stack = [1]
num=3 1<3? yes freq={1:3} stack=[3]
num=4 3<4? yes freq={1:3, 3:4} stack=[4]
num=2 4<2 no stack =[4,2]

freq={1:3, 3:4, 2:-1, 4:-1}

loop over nums1
freq[4]=-1 freq[1]=3 and freq[2]=-1

[-1,3,-1]


"""
