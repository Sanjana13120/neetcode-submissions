class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if not stack:
                    return False

                top = stack.pop()

                if (
                    s[i] == ")"
                    and top != '('
                    or s[i] == "]"
                    and top != '['
                    or s[i] == "}"
                    and top != '{'
                ):
                    return False

        return len(stack) == 0


"""
tc: O(n)
sc: O(n)

Input: s = "([{}])"

stack = [ ([{ ]

Input: s = "[(])"

stack = [ [( ]

top= ( and s[2]=] (!=] return false

"""
