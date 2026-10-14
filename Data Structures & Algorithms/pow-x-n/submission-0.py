class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = abs(n)
            x = 1 / x

        ans = 1

        while n != 0:
            if n % 2 == 1:
                ans *= x

            x *= x
            n //= 2

        return ans


"""
tc: O(logn)
sc: O(1)

Approach: Binary Exponentiation (Exponentiation by Squaring) 

Input: x = 2.00000, n = 5

2^5=32

ans=1

5!=0?   
    5%2==1? yes so ans*=x
    ans=2
    n=2
    x=4

2!=0? 
    2%2==0? so x=x*x=16
    n=2//2=1

1!=0?
    1%2==1? so ans*=x
    ans=2*16=32


----------------------------------------------------------------------
Input: x = 1.10000, n = 10
ans=1

10!=0?
    10%2==0? so x=x*x=1.21
    n=10//2=5

5!=0? 
    5%2==1? ans=1.21
    x=1.4641
    n=5//2=2

2!=0?
    2%2==0? x=2.14358881
    n=2//2=1

1!=0?
    1%2==1? ans=2.5937424601
    x=4.59497298636
    n=0

return ans =2.59374





"""
