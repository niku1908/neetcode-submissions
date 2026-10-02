class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for i in range(len(tokens)):
            # print(stack)
            ele =tokens[i]
            if ele in ("+","-","*","/"):
                if ele=="+":
                    val = stack.pop()
                    val_another = stack.pop()
                    stack.append(val+val_another)
                elif ele=="-":
                    val = stack.pop()
                    val_another = stack.pop()
                    stack.append(-val+val_another)
                elif ele=="*":
                    val = stack.pop()
                    val_another = stack.pop()
                    stack.append(val*val_another)
                elif ele=="/":
                    val = stack.pop()
                    val_another = stack.pop()
                  
                    stack.append(int(val_another/val))

            else:
                stack.append(int(ele))

        return stack[-1]