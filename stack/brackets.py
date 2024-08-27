from stack.stack import Stack
s=Stack()
def is_balanced(brackets):
    stack = Stack()
    for bracket in brackets:
        if bracket in ['(', '[', '{']:
            stack.push(bracket)
        elif bracket in [')', ']', '}']:
            if stack.is_empty():
                return False
            top = stack.pop()
            if (bracket == ')' and top != '(') or (bracket == ']' and top != '[') or (bracket == '}' and top != '{'):
                return False
    return stack.is_empty()

brackets = "[](([{()}]))"
if is_balanced(brackets):
    print("Brackets are balanced")
else:
    print("Brackets are not balanced")