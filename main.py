from Ex3 import MinStack

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack = MinStack()
    stack.push(-3)
    stack.push(0)
    stack.push(5)
    print_hi('PyCharm')
    print(stack.get_min())
    print(stack.top())


