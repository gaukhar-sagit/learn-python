# Task: Conditional Statements
# Description: Print the smallest number from a strictly increasing subsequence
# The program compares a, b, c, d and prints the minimum based on the increasing pattern

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < b < c < d:
    print(a)
else:
    if b < c < d:
        print(b)
    else:
        if c < d:
            print(c)
        else:
            print(d)

# Source: Stepik "Programming in Python"
# Topic: Conditional statements (if-else)
