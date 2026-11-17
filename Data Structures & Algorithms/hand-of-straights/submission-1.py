class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

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
tc: O(n+klogk)
    - Building frequency map: O(n)
    - Sorting unique keys: O(k log k)
    - Processing all groups: O(n)
    - Overall: O(n + k log k)

sc: O(k)
    - Frequency map: O(k)
    - Sorted unique keys: O(k)


n = total number of cards.
k = number of unique card values.

goal - Return true if it's possible to rearrange the cards into groups so that each group is of size groupSize and card values are consecutively increasing by 1, otherwise, return false.

Approach: Greedy + HashMap (Frequency Counter)
1. Check if len(hand) is divisible by groupSize. If not, return False because every group must contain exactly groupSize cards.
2. Build a frequency map using Counter to store the count of each card.
3. Sort the unique card values in ascending order so that we always process the smallest available card first.
4. Iterate through the sorted keys:
   - If freq[num] == 0, skip it because the card has already been used.
   - Otherwise, store its frequency in count. This represents how many groups must start with the current card.
5. Iterate through the next groupSize consecutive card values:
   - Check whether freq[num + i] >= count.
   - If not, return False because there aren't enough cards to form the required groups.
   - Otherwise, decrement freq[num + i] by count because those cards are now consumed.
6. If all cards are processed successfully, return True.


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
num=4 0==0? skip
num=5 0==0? skip






"""
