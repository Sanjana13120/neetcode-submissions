class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temperature, index = stack.pop()
                res[index] = i - index

            stack.append((temperatures[i], i))

        return res


"""
tc: O(n)
sc: O(n)

goal - find the no of days until the next warm temparature

Approach: Monotonic Stack

1. Initialize res = [0] * n  and stack = [] storing (temperature, index).
We store the index because when a warmer temperature arrives, we need to know how many positions/days apart the two temperatures are.
2. For each temperature:
   - While current temperature > temperature at stack top:
       - Pop (temp, idx)
       - res[idx] = current_index - idx
3. Push (current_temp, current_index) onto the stack.
4. Elements remaining in the stack have no warmer day, so their result remains 0.

Input: temperatures = [30,38,30,36,35,40,28]
for 30 next temp is 38 so 1 day (1-0)
38 -> 30,36,35,40 - 4  (5-1)
30 ->36 - 1   (3-2)
36->35,40 - 2 days (5-3)
35->40 - 1 day  (5-4)
40 -> 0 days
28 -> 0 days

 0  1  2  3  4  5  6
30 38 30 36 35 40 28

res=[0 0 0 0 0 0 0]

stack = []

i=0 stack = [(30,0)]
i=1  38>30? yes so pop 30 
    stack = [(38,1)]
    res[0] = i-0=1-0=1 res=[1 0 0 0 0 0 0]

i=2 30>38? stack = [(38,1), (30,2)]

i=3 36>30? yes stack = [(38,1)]
    res[2]=i-2=3-2=1 res=[1 0 1 0 0 0 0]
    36>38? no 
    stack = [(38,1), (36,3)]

i=4 35>36? no stack = [(38,1), (36,3), (35,4)]

i=5 40>35? yes stack = [(38,1), (36,3)]
    res[4]= 5-4=1 res=[1 0 1 0 1 0 0]
    40>36? yes stack = [(38,1)] 
    res[3]= 5-3=2 res=[1 0 1 2 1 0 0]
    40>38? yes stack=[]
    res[1]=5-1=4  res=[1 4 1 2 1 0 0]
    
    stack = [(40,5)]

i=6 28>40? no

finally res=[1 4 1 2 1 0 0]



"""
