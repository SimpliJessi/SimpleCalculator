num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
action = str(input("Choose action: Add(a), Sub(s), Mult(m), Div(d) -> "))

print("the result is ",end="")
if action == "a":
    print(num1+num2)
elif action == "s":
    print(num1-num2)
elif action == "m":
    print(num1*num2)
else:
    print(num1/num2)    