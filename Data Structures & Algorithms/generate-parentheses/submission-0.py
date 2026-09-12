class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_bracket, close_bracket, brackets):
            if open_bracket + close_bracket == 2 * n:
                res.append(brackets)
                return

            if open_bracket < n:
                backtrack(open_bracket + 1, close_bracket, brackets + "(")
            if open_bracket > close_bracket:
                backtrack(open_bracket, close_bracket + 1, brackets + ")")

        backtrack(0, 0, "")
        return res


"""
tc: O(n * C_n)
tc: O(n * C_n)

C_n is the nth Catalan number.

n=3

((())), ((),()) and so on.......

so n=3 6 brackets
n=2 4 brackets
n=4 8 brackets

approach: backtrack/recursion

open and close

n=3 i can add 3 open brackets -- (((

( - open < n, I am allowed to choose (.
) - open > close?  I am allowed to choose ).

base condition - if open + close == 2*n stop generating

((())))

"""
