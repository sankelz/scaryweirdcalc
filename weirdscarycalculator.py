print ("hi! welcome to the calculator i wish i'd had with me in my geometry class!")
inquiry = str(input("do you wanna find the midpoint?"))
if (inquiry == "yes"):
    x1 = int(input("first x-coordinate:"))
    y1 = int(input("first y-coordinate:"))
    x2 = int(input("second x-coordinate:"))
    y2 = int(input("second y-coordinate:"))
    print ("x is:")
    print ((x1+x2)/2)
    print ("y is:")
    print ((y1+y2)/2)
    inquiry = str(input("what do else you want to do?"))
else:
    calculator = str(input("well, do you want a regular calculator then?"))
    if (calculator == "yes"):
        print ("ok")
inquiry = str(input("what do you want to do? (you need. to do arithmetic)"))
if (inquiry == "add"):
    a = int(input('first number: '))
    b = int(input('second number: '))
    sum = a + b
    print ("your sum is: " + str(sum))
if (inquiry == "subtract"):
    a = int(input('first number: '))
    b = int(input('second number: '))
    sum = a - b
    print ("your remainder is: " + str(sum))
if (inquiry == "multiply"):
    a = int(input('first number: '))
    b = int(input('second number: '))
    sum = a * b
    print ("your product is: " + str(sum))
if (inquiry == "divide"):
    a = int(input('first number: '))
    b = int(input('second number: '))
    sum = a / b
    print ("your answer is: " + str(sum))


