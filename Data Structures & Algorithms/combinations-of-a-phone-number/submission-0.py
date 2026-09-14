class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        freq = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return

            for c in freq[digits[i]]:
                backtrack(i + 1, curr_str + c)

        if digits:
            backtrack(0, "")

        return res


"""
tc: O(n x 4^n)
sc: O(n x 4^n)  including output
    O(n) excluding output.

digits- 2 to 9
except digit 1 all are mapped to char


goal: all possible combinations of digits

Input: digits = "34"

freq = {"2" : "abc", "3" : "def", "4" : "ghi", "5" :"jkl", "6' :"mno", "7" : "pqrs", "8": "tuv", "9": "wxyz"}

3: def and 4: ghi

["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]

Approach: recursion/backtracking

base: len(currstr) == len(digits)
        append to res and return


backtrack(0,"")
    loop c over freq[digits[i]]  ie c = 3
        backtrack(1,d)
            loop c in freq[digits[1]] ie= c=4
                backtrack(2,dg)
                    len(dg)==len(digits)? yes so res=["dg"]
                backtrack(2,dh)
                    res=["dg", "dh"]
                backtrack(2,di)
                    res=["dg", "dh","di"]
        backtrack(1,e)
            loop c in freq[digits[1]] -- c=4
                backtrack(2,eg)
                    res=["dg", "dh","di","eg"]
                backtrack(2,eh)
                    res=["dg", "dh","di","eg","eh"]
                backtrack(2,ei)
                    res=["dg", "dh","di","eg","eh","ei"]
        backtrack(1,f)
            and so on......

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
                    


"""
