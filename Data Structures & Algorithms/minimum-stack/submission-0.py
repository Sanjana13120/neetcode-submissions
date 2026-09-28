class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack or self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


"""
For  MinStack:

tc: 
push() → O(1) time
pop() → O(1) time
top() → O(1) time
getMin() → O(1) time

Overall: O(1) per operation

Sc:
stack → O(n)
minstack → O(n)
Total auxiliary space → O(n)


-------------------------------------------------

stack = []
minstack = []

push(1)

stack= [1]
minstack = [1]

push(2)
stack = [1 2]
minstack[-1]>2? 1>2 no so minstack = [1]

push(0)
stack = [1 2 0]
minstack[-1]>0 1>0? yes so minstack =[1 0]

getmin - minstack[-1] -- returns 0

pop()
val = 0
stack= [1 2]
minstack = [1]

top 
stack[-1] =2 

getmin()
returns 1



"""
