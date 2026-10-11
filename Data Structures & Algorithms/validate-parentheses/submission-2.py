class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["{","[","("]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                char2 = stack.pop()
                if char == "}" and char2 == "{":
                    continue 
                elif char == "]" and char2 == "[":
                    continue 
                elif char == ")" and char2 == "(":
                    continue 
                else:
                    return False

        if len(stack) != 0:
            return False
        return True
