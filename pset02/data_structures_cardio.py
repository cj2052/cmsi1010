import unittest


def third_element(t):
    """
    If t is a tuple with at least three elements, returns the third
    element. If t is not a tuple, raise a TypeError. If fewer than
    three elements, raise an IndexError.
    """
    if not isinstance(t, tuple): 
        raise TypeError("Input must be a tuple")
    if len(t) < 3:
        raise IndexError ("Input must have 3 or more elements")
    return t[2]


def reverse_pair(t):
    """
    if t is a tuple of two elements, returns a new tuple with the
    elements in reverse order. If t is not a tuple, raise a TypeError.
    If t is a tuple with more or fewer than two elements, raise a
    ValueError.
    """
    if not isinstance(t, tuple):
        raise TypeError("Input must be a tuple")
    if len(t) != 2:
        raise ValueError("Input must contain exactly two elements")
    new_tuple = t[::-1]
    return new_tuple
    

def middle_element_of_list(a):
    """
    If a is a list with an odd number of elements, returns the
    middle element. If a is a list with an even number of elements,
    return the leftmost middle element. If a is a list with no
    elements, raise an IndexError. If a is not a list, raise a
    TypeError.
    """
    if a == "":
        raise IndexError("List must contain at least one item")
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    if len(a) % 2 == 0: 
        return a[len(a)//2 - 1] 
    return a[len(a)//2]
    


def unique_elements(a):
    """
    Returns a set of unique elements from the input list a.
    If a is not a list, raise a TypeError.
    """
    unique_elements = set()
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    for word in a:
        if word not in unique_elements:
            unique_elements.add(word)
    return unique_elements


def contains_duplicates(a):
    """
    Returns True if the input list a contains any duplicate elements,
    and False otherwise. If a is not a list, raise a TypeError.
    """
    unique_elements = set()
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    for word in a:
        if word in unique_elements:
            return True
        else:
            unique_elements.add(word)
    return False

def is_superset(a, b):
    """
    Returns True if set a is a superset of set b, and False otherwise.
    If either a or b is not a set, raise a TypeError.
    """
    
    if not (isinstance(a, set) and isinstance(b, set)):
        raise TypeError("Both arguments must be sets")
    for count in b:
        if count not in a:
            return False
    else:
        return True


def is_subset(a, b):
    """
    Returns True if set a is a subset of set b, and False otherwise.
    If either a or b is not a set, raise a TypeError.
    """
    if not (isinstance(a, set) and isinstance(b, set)):
        raise TypeError("Both arguments must be sets")
    for count in a:
        if count not in b:
            return False
    else:
        return True


def is_disjoint(a, b):
    """
    Returns True if sets a and b are disjoint (i.e., have no elements in common),
    and False otherwise. If either a or b is not a set, raise a TypeError.
    """
    if not (isinstance(a, set) and isinstance(b, set)):
        raise TypeError("Both arguments must be sets")
    for count in a:
        if count in b:
            return False
        else: 
            return True
        

def most_frequent_value_or_values(d):
    """
    Returns the value or values that appear most frequently in the
    dictionary d. If there are multiple values with the same maximum
    frequency, return them as a set. If d is empty, return None.
    If d is not a dictionary, raise a TypeError.
    """
    frequencies = dict()
    max_val = 0
    max_values = set()
    if not isinstance(d, dict):
        raise TypeError("Input must be a dictionary")
    if d == {}:
        return None
    for value in d.values():
        frequencies[value] = frequencies.get(value, 0) + 1
    max_val = max(frequencies.values())
    for key, value in frequencies.items():
        if value == max_val:
            max_values.add(key)
    return max_values  


def key_is_in_both_dictionaries(d1, d2, key):
    """
    Returns True if the key is present in both dictionaries d1 and d2,
    and False otherwise. If either d1 or d2 is not a dictionary,
    raise a TypeError.
    """
    if not (isinstance(d1, dict) and isinstance(d2, dict)):
        raise TypeError("First two inputs must be dictionaries")
    return key in (d1 and d2)



def word_frequencies(s):
    """
    Returns a dictionary with the frequency of each word in the string s.
    The keys of the dictionary are the words, and the values are the
    number of times each word appears in the string.

    A word is defined as a sequence of characters separated by spaces.
    You can implement this function using the split method.

    If s is not a string, raise a TypeError.
    """
    words = {}
    if not isinstance(s, str):
        raise TypeError("Inputs must be strings")
    for count in s.split():
        if count not in words: 
            words[count] = 0
        words[count] += 1
    return words   


class TestDataStructuresCardio(unittest.TestCase):
    def test_third_element(self):
        self.assertEqual(third_element((1, 2, 3, 4)), 3)
        with self.assertRaises(IndexError):
            third_element((1, 2))
        with self.assertRaises(IndexError):
            third_element((1,))
        with self.assertRaises(TypeError):
            third_element([1, 2, 3])
        with self.assertRaises(TypeError):
            third_element("not a tuple")

    def test_reverse_pair(self):
        self.assertEqual(reverse_pair((1, 2)), (2, 1))
        with self.assertRaises(ValueError):
            reverse_pair((1, 2, 3))
        with self.assertRaises(ValueError):
            reverse_pair((1,))
        with self.assertRaises(TypeError):
            reverse_pair([1, 2])
        with self.assertRaises(TypeError):
            reverse_pair("not a tuple")

    def test_middle_element_of_list(self):
        self.assertEqual(middle_element_of_list([1, 2, 3]), 2)
        self.assertEqual(middle_element_of_list([1, 2]), 1)
        self.assertEqual(middle_element_of_list([10, 20, 30, 40]), 20)
        self.assertEqual(middle_element_of_list([5] * 500), 5)
        with self.assertRaises(IndexError):
            middle_element_of_list([])
        with self.assertRaises(TypeError):
            middle_element_of_list((1, 2))
        with self.assertRaises(TypeError):
            middle_element_of_list("not a list")

    def test_unique_elements(self):
        self.assertEqual(unique_elements([1, 2, 2, 3]), {1, 2, 3})
        self.assertEqual(unique_elements([1, 1, 1]), {1})
        self.assertEqual(unique_elements([]), set())
        self.assertEqual(unique_elements([1, 2, 3, 4, 5]), {1, 2, 3, 4, 5})
        self.assertEqual(unique_elements(
            [False, 3, "dog", False, "dog"]), {False, 3, "dog"})
        with self.assertRaises(TypeError):
            unique_elements("not a list")
        with self.assertRaises(TypeError):
            unique_elements({1, 2, 3})

    def test_contains_duplicates(self):
        self.assertTrue(contains_duplicates([1, 2, 2]))
        self.assertFalse(contains_duplicates([1, 2, 3]))
        with self.assertRaises(TypeError):
            contains_duplicates("not a list")
        with self.assertRaises(TypeError):
            contains_duplicates({1, 2, 3})

    def test_is_superset(self):
        self.assertTrue(is_superset({1, 2}, {1}))
        self.assertFalse(is_superset({1}, {1, 2}))
        with self.assertRaises(TypeError):
            is_superset({1}, "not a set")

    def test_is_subset(self):
        self.assertTrue(is_subset({1}, {1, 2}))
        self.assertFalse(is_subset({1, 2}, {1}))
        with self.assertRaises(TypeError):
            is_subset("not a set", {1})

    def test_is_disjoint(self):
        self.assertTrue(is_disjoint({1}, {2}))
        self.assertFalse(is_disjoint({1}, {1}))
        with self.assertRaises(TypeError):
            is_disjoint({1}, "not a set")
        with self.assertRaises(TypeError):
            is_disjoint("not a set", {1})

    def test_most_frequent_value_or_values(self):
        self.assertEqual(most_frequent_value_or_values(
            {'a': 1, 'b': 2, 'c': 1}), {1})
        self.assertEqual(most_frequent_value_or_values(
            {'a': 1, 'b': 2, 'c': 2}), {2})
        self.assertEqual(most_frequent_value_or_values(
            {'a': 1, 'b': 1, 'c': 2, 'd': 2}), {1, 2})
        self.assertEqual(most_frequent_value_or_values({}), None)
        with self.assertRaises(TypeError):
            most_frequent_value_or_values("not a dict")

    def test_key_is_in_both_dictionaries(self):
        self.assertTrue(key_is_in_both_dictionaries(
            {'a': 1, 'b': 2}, {'b': 3, 'c': 4}, 'b'))
        self.assertFalse(key_is_in_both_dictionaries(
            {'a': 1}, {'b': 2}, 'a'))
        with self.assertRaises(TypeError):
            key_is_in_both_dictionaries("not a dict", {'b': 2}, 'b')
        with self.assertRaises(TypeError):
            key_is_in_both_dictionaries({'a': 1}, "not a dict", 'a')

    def test_word_frequencies(self):
        self.assertEqual(word_frequencies("hello world hello"),
                         {'hello': 2, 'world': 1})
        self.assertEqual(word_frequencies("a b a c b a"),
                         {'a': 3, 'b': 2, 'c': 1})
        self.assertEqual(word_frequencies("test test test"), {'test': 3})
        self.assertEqual(word_frequencies(""), {})
        with self.assertRaises(TypeError):
            word_frequencies(12345)
        with self.assertRaises(TypeError):
            word_frequencies(["not", "a", "string"])
        with self.assertRaises(TypeError):
            word_frequencies({"not": "a string"})


if __name__ == "__main__":
    unittest.main()