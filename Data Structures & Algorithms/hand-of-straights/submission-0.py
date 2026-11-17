class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        key = sorted(freq)

        for num in key:
            if freq[num] == 0:
                continue

            count = freq[num]
            for i in range(0, groupSize):
                if freq[num + i] < count:
                    return False

                freq[num + i] -= count

        return True


"""
goal - Return true if it's possible to rearrange the cards into groups so that each group is of size groupSize and card values are consecutively increasing by 1, otherwise, return false.

Approach:



Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4

1 2 4 2 3 5 3 4

freq= {1:1 2:2 4:2 3:2 5:1}
key = [1,2,3,4,5]

num=1 count=1
    i=0 freq[1]=1<1?no  freq= {1:0 2:2 4:2 3:2 5:1}
    i=1 freq[2]=2<1? no freq= {1:0 2:1 4:2 3:2 5:1}
    i=2 2<1?no freq= {1:0 2:1 4:2 3:2 5:1}
    i=3 2<1?no   freq={1:0 2:1 4:1 3:1 5:1}

num=2 count=1
    i=0 1<1?no  freq={1:0 2:0 4:1 3:1 5:1}
    i=1 1<1? no  freq={1:0 2:0 4:1 3:0 5:1}
    i=2 1<1? no  freq={1:0 2:0 4:0 3:0 5:1}
    i=3 1<1?no   freq={1:0 2:0 4:0 3:0 5:0}

num=3 0==0? skip
num=3 0==0? skip






"""
