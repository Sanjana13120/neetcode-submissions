class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            currsum = numbers[left] + numbers[right]

            if currsum == target:
                return [left + 1, right + 1]

            elif currsum < target:
                left += 1

            else:
                right -= 1


"""
tc: O(n)
sc: O(1)

goal - return index of num that add to target

given arr is sorted

approach: 2 pointers

1 2 3 4 
s e

start = 0
end=3
0<3
currsum=5 ==3? 5>3? end=2

0<2? yes
currsum=1+3=4==3? no 4>3? so end=1

0<1
currsum=1+2=3==3? yes return start+1, right+1 --> [1,2]


"""
