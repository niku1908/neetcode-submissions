class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()

            curr = curr.children[char]
        curr.is_word = True

    def dfs(self, index, curr, word):

        current = curr

        for i in range(index, len(word)):

            if word[i]=='.':
                for child in current.children.values():
                    if self.dfs(i+1, child, word):
                        return True

                return False

            else:
                if word[i] not in current.children:
                    current.children[word[i]]=TrieNode()

                current = current.children[word[i]]

        return current.is_word


    def search(self, word: str) -> bool:
        curr = self.root

        return self.dfs(0, curr, word)

        
