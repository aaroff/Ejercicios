# Multiplier and multiplying input

num = int(input("Enter a number to multiply: "))
num2 = int(input("Enter a second number to multiply: "))
result = num * num2

# Result printing and comparison with "50"

print("The result from multiplying", num, "and", num2, "equals:", result)
if result > 50:
    print("This number is greater than 50")
elif result < 50:
    print("This number is smaller than 50")
elif result == 50:
    print("This number is equal to 50")

# Subtrahend input

num3 = int(input("Enter a number to substract from the desired multiplication: "))
result2 = result - num3

# Second result printing and positive/negative definition

if result2 > 0:
    print("After substracting", num3, ", the result is", result2, "which is a positive number")
    print("Thanks for using the program!")
elif result2 < 0:
    print("After substracting", num3, ", the result is", result2, "which is a negative number")
    print("Thanks for using the program!")
elif result2 == 0:
    print("After substracting", num3, ", the result is", result2,)
    print("Thanks for using the program!")