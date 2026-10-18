class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            # c = bin(i).count('1')
            num = i

            while num != 0:
                res[i] += 1
                num &= num - 1

        return res


"""
tc: O(nlogn)
sc: O(n)

"""
