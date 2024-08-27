from stack.stack import Stack

def reverse_string(string):
    stack = Stack()  # Create an instance of the Stack class

    # Push each character of the string onto the stack
    for char in string:
        stack.push(char)  # Use the push method of the Stack class to add characters to the stack

    reversed_string = ""

    # Pop each character from the stack to get the reversed string
    while not stack.is_empty():  # Use the is_empty method of the Stack class to check if the stack is empty
        reversed_string += stack.pop()  # Use the pop method of the Stack class to remove characters from the stack and add them to the reversed string

    return reversed_string

# Test the function
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)
