from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        queue = deque([(beginWord,1)])
        wordset = set(wordList)

        while queue:
            word, curr_lvl = queue.popleft()

            if word == endWord:
                return curr_lvl

            for i in range(len(word)):
                for c in range(97,123):
                    neighbor = word[:i] + chr(c) + word[i+1:]

                    if neighbor in wordset:
                        queue.append((neighbor, curr_lvl+1))
                        wordset.remove(neighbor)

        return 0  

'''
tc : O(NL**2)
sc : O(NL)

N = number of words
L = length of each word

Time: O(N x L²)
    L positions x 26 characters x O(L) string construction
    → O(N x L²)

Space: O(N x L)
    wordset + queue


given beginWord and endWord, and also a list of words wordList. 

goal : to transform beginWord into endWord provided that at exactly one position the words have a different character

return minimum number of words within the transformation sequence  else 0

Approach- BFS

1. Initialize: queue = [(beginWord, 1)]
               wordset = set(wordList)
2. While the queue is not empty:
    Remove (word, curr_level) from the front.
    If word == endWord, return curr_level.
3. Generate neighbors:
    Loop through every character position.
    Try every letter from a to z.
    Create the new word.
4. If the generated word exists in wordset:
    Add it to the queue with curr_level + 1.
    Remove it from wordset.
5. If the queue becomes empty without reaching endWord, return 0.

Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]

queue = [(cat,1)]
wordset = {bat, bag, sag, dag, dot}

next word is bat
bat in wordeset? add to queu
queue = [(bat,2)]
wordset = {bag, sag, dag, dot}

next word is bag
bag in wordeset? add to queue
queue = {(bag,3)}
wordset = {sag, dag, dot}

word is sag
sag in wordset? add to queue
queue = {(sag,4)}
wordset = {dag, dot}

sag==endword return 4

----------------------------------------------------------------------------------------------------------------
Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sat","dag","dot"]

queue = {(cat,1)}
wordset = {"bat","bag","sat","dag","dot"}

cat -> bat
bat in wordset? yes 
queue = {(bat,2)}
wordset = {"bag","sat","dag","dot"}

cat -> sat
sat in wordset? yes
queue = {(bat,2), (sat,2)}
wordset = {"bag","dag","dot"}

process (bat,2)
bat--> sat but not in wordset 
bat --> bag?
queue = {(sat,2), (bag,3)}
wordset = {"dag","dot"}

process (sat,2)
sat -> sag but not in wordset

process(bag,3)
bag--> bat not in wordset
bag -->sag not in wordset
bag -->dag?
queue = {(dag,4)}
wordset = {"dot"}

after processing all and queue empty 
we dint find endWord sag
so return 0








'''