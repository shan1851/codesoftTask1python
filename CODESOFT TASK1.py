a = int(input("Enter Your First Number:"))
b = int(input("Enter Your Second Number:"))
c = str(input("Select a operator(+,-,/,*,//:"))
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
elif c == "**":
    print(a**b)
elif c == "//":
    print(a//b)
else:
    print("Error")
