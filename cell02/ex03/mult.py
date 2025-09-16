number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
answer = number_1 * number_2
print(number_1, "x", number_2, "=", answer)
if answer < 0:
    print("The result is negative.")
elif answer > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")