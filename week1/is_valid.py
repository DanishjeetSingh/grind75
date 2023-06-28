def is_valid( s: str) -> bool:
    stack = []

    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            # if stack is empty then the order of parentheses is wrong, return false
            if not stack:
                return False
            # if the match is right then keep popping from the stack and keep moving on
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                # if you have added a open parentheses to the stack, but the right closing paren isn't found, return false
                return False

    # at the end if the stack is empty then return true, else False
    return not stack