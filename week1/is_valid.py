def is_valid(self, s: str) -> bool:
    stack = []

    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

    return not stack