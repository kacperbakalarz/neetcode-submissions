
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stack2 = []
        for token in tokens:
            if token in ["+","-","*","/"]:
                stack2.append(token)
            else:
                stack.append(int(token))
            if len(stack) >= 2 and len(stack2) == 1:
                a = stack.pop()
                b = stack.pop()
                c = stack2.pop()
                if c == "+":
                    stack.append(a+b)
                elif c == "-":
                    stack.append(b-a)
                elif c == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
        return stack.pop()