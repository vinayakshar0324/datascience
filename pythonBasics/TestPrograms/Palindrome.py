# 131
# 101
# WAP to check if number is Palindrome or not

number = int(input("Enter The number to check for Palindrome:"))

temp = number

reverse = 0

while number > 0:
    digit = number%10
    reverse = reverse*10 + digit
    number = number // 10

if (temp == reverse):
    print("No. is Plaindrome Number")
else:
    print("No. is not a Plaindrome Number")
    