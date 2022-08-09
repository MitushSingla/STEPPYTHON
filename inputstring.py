# Take input from user
num = input("Enter any number : ")

# Reverse the number
reverse = str(num)[::-1]

# Empty print statement for new line
print()

# Check for palindrome
if reverse == num:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")