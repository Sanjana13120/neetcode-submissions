class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))

        return stack[0]


"""
tc: O(n)
sc: O(n)

goal - result of the expression

Input: tokens = ["1","2","+","3","*","4","-"]

approach: stack


stack = [5]

i = -
b=4
a=9

-----------------------------------------------------

tokens = ["4","13","5","/","+"]

stack = [6]

i=+

b=2
a=4


"""
