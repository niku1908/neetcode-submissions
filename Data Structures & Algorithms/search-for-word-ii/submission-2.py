class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Solution:

    def check(self, board,i,j, ans, root):
        if root.is_word:
            ans.append(root.word)
            root.is_word = False
            

        if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
            return

        if board[i][j]=='#' or board[i][j] not in root.children:
            return

        char = board[i][j]

        

        board[i][j]='#'

        self.check(board, i+1,j, ans, root.children[char])
        self.check(board, i-1,j, ans, root.children[char])
        self.check(board, i,j+1, ans, root.children[char])
        self.check(board, i,j-1, ans, root.children[char])

        board[i][j]=char


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char]=TrieNode()

                curr = curr.children[char]

            curr.is_word = True
            # print(word)
            curr.word = word

        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    self.check(board,i,j, ans, root)

        return ans

                
        