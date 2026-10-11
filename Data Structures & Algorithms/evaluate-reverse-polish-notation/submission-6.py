
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+","-","*","/"]:
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    c = token
                    if c == "+":
                        stack.append(a+b)
                    elif c == "-":
                        stack.append(b-a)
                    elif c == "*":
                        stack.append(a*b)
                    else:
                        stack.append(int(b/a))
            else:
                stack.append(int(token))
            
        return stack.pop()