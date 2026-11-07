from Ex3 import MinStack
from Ex5 import UndergSys

def test():
    stack = MinStack()
    stack.push(-3)
    stack.push(0)
    stack.push(5)
    assert stack.get_min() == -3
    print(stack.get_min())
    print(stack.top())


    metro = UndergSys()
    metro.chek_in(45, "Volokolamsk", 3)
    metro.check_out(45, "Streshnevo", 15)

    metro.chek_in(27, "Saint-Peterburg", 10)
    metro.check_out(27, "Moscow", 20)

    assert metro.get_time("Saint-Peterburg", "Moscow") == 10.0
    assert metro.get_time("Podolsk", "Moscow") is None

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    test()






