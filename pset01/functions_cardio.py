def is_odd(n):
    """
    Returns True if n is odd, False otherwise.
    """
    # replace the pass statement with your code
    if n % 2 == 0:
        return False
    else:
        return True
    


def median_of_three(a, b, c):
    """
    Returns the median of three numbers a, b, and c.
    """
    # replace the pass statement with your code
    
    if a>b:
        if a>c:
            if b>c:
                return b
            else:
                return  c
        else:
            return  a
    elif a>c:
        return a 
    elif b>a:
        if b>c:
           return c
        else:
            return b
    elif c>a:
        return b
    else:
        return a
    #print("The median of", a, ",", b, ", and", c, "is", median )
        
median_of_three(33, 0, 70)
median_of_three(20, 20, 20)
median_of_three(1, 0, -1)
median_of_three(9, 900, 43)



def is_palindrome(s):
    """
    Returns True if the string s is a palindrome, False otherwise.

    A palindrome reads the same forwards and backwards. You can
    implement it as a simple check to see if s is equal to its
    reversal.
    """
    # replace the pass statement with your code
    if s.replace(" ", "") == s[::-1].replace(" ", ""):
        return True
        #palindrome = True
        #print (s, "is a palindrome")
    else:
        return False
        #palindrome = False
        #print( s, "is not a palindrome")

is_palindrome("taco cat")
is_palindrome("apple")
is_palindrome("oogplpgoo")



def factorial(n):
    """
    Returns the factorial of n (n!).

    The factorial of a non-negative integer n is the product of all
    positive integers less than or equal to n. Please implement this
    function with a for loop.
    """
    # replace the pass statement with your 
    factorial = 1
    for count in range(1, n + 1):
       factorial *= count 
    return factorial

factorial(6)


def count_of_latin_vowels(s):
    """
    Returns the number of vowels in the string s.

    The vowels are 'a', 'e', 'i', 'o', and 'u'. You can implement this
    function using a for loop to iterate through the string.
    """
    # replace the pass statement with your code
    vowels = 0
    for count in s:
        if count in "aeiouAEIOU":
            vowels = vowels + 1
    return vowels

count_of_latin_vowels('asdfjhoqieu')



def longest_string(strings):
    """
    Returns the longest string from a list of strings.

    If there are multiple strings with the same maximum length, return
    the first one encountered.
    """
    longest_string = ""
    for count in strings[::]:
        if len(count) > len(longest_string):
            longest_string = count 
    return longest_string
     
        




def word_frequencies(s):
    """
    Returns a dictionary with the frequency of each word in the string s.
    The keys of the dictionary are the words, and the values are the
    number of times each word appears in the string.

    A word is defined as a sequence of characters separated by spaces.
    You can implement this function using the split method.
    """
    # replace the pass statement with your code
    words = {}
    for count in s.split():
        if count not in words: 
            words[count] = 0
        words[count] += 1
    return words            

word_frequencies("the lazy green alligator took it's lazy green tail to the lazy lake")

assert is_odd(3) == True
assert is_odd(8) == False
assert is_odd(-3) == True
assert is_odd(-8) == False

assert median_of_three(1, 2, 3) == 2
assert median_of_three(1, 3, 2) == 2
assert median_of_three(2, 1, 3) == 2
assert median_of_three(2, 3, 1) == 2
assert median_of_three(3, 1, 2) == 2
assert median_of_three(3, 2, 1) == 2

assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(6) == 720
assert factorial(20) == 2432902008176640000

assert is_palindrome("racecar") == True
assert is_palindrome("hello") == False
assert is_palindrome("madam") == True
assert is_palindrome("python") == False

assert count_of_latin_vowels("hello world") == 3
assert count_of_latin_vowels("aeiou") == 5
assert count_of_latin_vowels("xyz") == 0
assert count_of_latin_vowels("Python programming") == 4
assert count_of_latin_vowels("Aeiou") == 5

assert longest_string(["apple", "banana", "cherry"]) == "banana"
assert longest_string(["cat", "dog", "elephant"]) == "elephant"
assert longest_string(["short", "longer", "longest"]) == "longest"
assert longest_string(["a", "ab", "abc"]) == "abc"
assert longest_string(["one", "two", "three", "four"]) == "three"

assert word_frequencies("hello world hello") == {'hello': 2, 'world': 1}
assert word_frequencies("a b a c b a") == {'a': 3, 'b': 2, 'c': 1}
assert word_frequencies("test test test") == {'test': 3}
assert word_frequencies("") == {}