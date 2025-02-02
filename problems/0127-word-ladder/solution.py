from collections import defaultdict
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        Time Complexity : O(N*M^2), where N is the number of words and
        M is the length of the word.

        Space Complexity : O(N*M^2)
        '''

        '''
        All words are guaranteed to be of same length.
        In order to continue the Breath First Search(BFS) for shortest path,
        we need to know the children of *it, h*t, and hi*.
        For that we create a hash-map,
        { *ot : hot, dot, lot
			h*t : hot
			ho* :hot
			d*t : dot
			do* : dot, dog
			*og : dog, log, cog
			d*g : dog
			l*t : lot
			lo* : lot, log
			l*g : log
			c*g: cog
			co* : cog 
		}
        To avoid duplicate calculation, 
        we keep a visited map,  
        if the word in the visited map, 
        we skip the word, i.e. don't append the word into the queue.
        if the word not in the visited map, 
        we put the word into the visited map, and append the word into the queue.
        '''
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        N = len(beginWord)
        all_combinations_map = defaultdict(list)
        for word in wordList:
            for i in range(N):
                all_combinations_map[word[:i] + "*" + word[i+1:]].append(word)

        visit = set()
        visit.add(beginWord)
        queue = deque()
        queue.append(beginWord)
        length = 1
        while queue:
            for j in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return length
                for i in range(N):
                    for neighbor in all_combinations_map[curr[:i] + "*" + curr[i+1:]]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            queue.append(neighbor)
            length+=1

        return 0



        
