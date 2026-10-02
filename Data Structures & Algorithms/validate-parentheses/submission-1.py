class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if not stack:
                if s[i] in (']','}',')'):
                    return False

                else:
                    stack.append(s[i])

            else:
                if s[i]=='}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                elif s[i]==']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                elif s[i]==')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(s[i])
        if stack:
            return False
        return True