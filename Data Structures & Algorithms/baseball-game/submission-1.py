class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        q = deque()
        for i in ops:
            print(q)
            if not q:
                q.append(int(i))
            else:
                if i == "+":
                    a = q.pop()
                    b = q.pop()
                    c = a+b
                    q.append(b)
                    q.append(a)
                    q.append(c)
                elif i=="D":
                    a = q.pop()
                    b = 2*a
                    q.append(a)
                    q.append(b)
                elif i=="C":
                    a = q.pop()
                else:
                    q.append(int(i))

        return sum(list(q))