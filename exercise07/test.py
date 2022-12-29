def function1(b):
    if b == 10:
        return


    print(b)
    function1(b+1)


function1(3)

b = 3
stack = []
stack.append(b)
while b != 10:
    print(b)
    b += 1
    stack.append(b)
    b = stack.pop()
