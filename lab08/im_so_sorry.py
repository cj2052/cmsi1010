def blocks(n): 
    return 0 if n<= 0 else blocks(n-1) + n


def print_count_down(n):
    if n<0:
        print("BOOM")
    else:
        print(n)
        print_count_down(n-1)

print_count_down(10)

def sum_of_digits(n):
    if n<10:
        return 0
    else:
        print(n)
        sum_of_digits(n//10 + n % 10)
sum_of_digits(1234)

def factorial(n):
    if n <= 0:
        return 1
    else:
       return factorial(n-1) * n

print(factorial(5))

def is_palindrome(s):
    if len(s) <= 1:
        return True
    else: 
        return s[0] == s[-1] and is_palindrome(s[1:-1])
    
print(is_palindrome("racecar"))
