print("Enter a number")
number = int(input(":"))
i = 0
while i <= 9:
    answer = number * i
    print(f"{number} x {i} = {answer}")
    i += 1