class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        seen = set(wordList)

        if endWord not in seen:
            return 0

        q = deque()
        q.append(beginWord)
        level = 1

        while q:
            size = len(q)
            
            while size:
                word = q.popleft()
                if word == endWord:
                    return level
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue
                        
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word in seen:
                            q.append(new_word)
                            seen.remove(new_word)
                size-=1
            level+=1
        return 0










