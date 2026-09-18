class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4
        sides = [0] * 4

        matchsticks.sort(reverse=True)

        def backtrack(i, sides):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if matchsticks[i] + sides[j] <= target:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1, sides):
                        return True
                    sides[j] -= matchsticks[i]

            return False

        return backtrack(0, sides)


"""
tc: O(4^n)
sc: O(n)

goal - Return true if you can make this square and false otherwise.

total- even-- i can make a square

Approach:

1. find the total length of matchsticks. taregt = total//4 since each side of square is equal
2. sides = [0 0 0 0]
3. backtrack(0,sides)
    loop j over sides
        compare if matchsticks[i]+sides[j]<= target
            updates sides[j]=matchsticks[i]+sides[j]
            backtrack(i+1,sides)
        if it doesnt match sides[j]-=matchsticks[i]

5. if i reaches len(matchsticks) : successfully all sides are equal to target return True
6. otherwise return false


matchsticks = [1,3,4,2,2,4]

total=16
target=4

sides= [0 0 0 0]

backtrack(0,sides)
    i=0 
        j=0
            1+0<=4?yes
            sides=[1 0 0 0]
            backtrack(1,sides)
                i=1
                    j=0 
                        1+3<=4? yes sides=[4 0 0 0]
                        backtrack(2,sides)
                            i=2
                                j=0
                                    8>=4 no
                                j=1
                                    0+4<=4?yes sides=[4 4 0 0]
                                    backtrack(3,sides)
                                        i=3
                                            j=0 x
                                            j=1 x
                                            j=2 0+2<=4?yes sides[4 4 2 0]
                                            backtrack(4, sides)
                                                i=4
                                                    j=0 x
                                                    j=1 x
                                                    j=2 2+2<=4 yes sides=[4 4 4 0]
                                                    backtrack(5,sides)
                                                        i=5
                                                            j=0x
                                                            j=1 x
                                                            j=2 x
                                                            j=3 0+4<=4? yes sides=[4 4 4 4]
                                                            backtrack(6,sidess) 
                                                                6==len(matchsticks)?yes 
                                                                    return True

------------------------------------------------------------------------------------------------------------------------
Input: matchsticks = [1,5,6,3]

total=15 is odd 
return false



"""
