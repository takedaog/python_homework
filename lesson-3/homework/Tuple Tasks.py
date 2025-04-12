# 1. Count Occurrences
def count_occurrences_tuple(tpl, element):
    return tpl.count(element)

# 2. Max Element
def max_element_tuple(tpl):
    return max(tpl)

# 3. Min Element
def min_element_tuple(tpl):
    return min(tpl)

# 4. Check Element
def check_element_tuple(tpl, element):
    return element in tpl

# 5. First Element
def first_element_tuple(tpl):
    return tpl[0] if tpl else None

# 6. Last Element
def last_element_tuple(tpl):
    return tpl[-1] if tpl else None

# 7. Tuple Length
def length_of_tuple(tpl):
    return len(tpl)

# 8. Slice Tuple
def slice_tuple(tpl):
    return tpl[:3]

# 9. Concatenate Tuples
def concatenate_tuples(tpl1, tpl2):
    return tpl1 + tpl2

# 10. Check if Tuple is Empty
def is_tuple_empty(tpl):
    return len(tpl) == 0

# 11. Get All Indices of Element
def all_indices_tuple(tpl, element):
    return [i for i, x in enumerate(tpl) if x == element]

# 12. Find Second Largest
def second_largest_tuple(tpl):
    unique = list(set(tpl))
    unique.sort(reverse=True)
    return unique[1] if len(unique) >= 2 else None

# 13. Find Second Smallest
def second_smallest_tuple(tpl):
    unique = list(set(tpl))
    unique.sort()
    return unique[1] if len(unique) >= 2 else None

# 14. Create a Single Element Tuple
def single_element_tuple(element):
    return (element,)

# 15. Convert List to Tuple
def list_to_tuple(lst):
    return tuple(lst)

# 16. Check if Tuple is Sorted
def is_tuple_sorted(tpl):
    return tpl == tuple(sorted(tpl))

# 17. Find Maximum of Subtuple
def max_of_subtuple(tpl, start, end):
    return max(tpl[start:end])

# 18. Find Minimum of Subtuple
def min_of_subtuple(tpl, start, end):
    return min(tpl[start:end])

# 19. Remove Element by Value
def remove_element_tuple(tpl, element):
    lst = list(tpl)
    if element in lst:
        lst.remove(element)
    return tuple(lst)

# 20. Create Nested Tuple
def create_nested_tuple(tpl, size):
    return tuple(tpl[i:i+size] for i in range(0, len(tpl), size))

# 21. Repeat Elements
def repeat_elements_tuple(tpl, times):
    return tuple(x for x in tpl for _ in range(times))

# 22. Create Range Tuple
def create_range_tuple(start, end):
    return tuple(range(start, end + 1))

# 23. Reverse Tuple
def reverse_tuple(tpl):
    return tpl[::-1]

# 24. Check Palindrome
def is_tuple_palindrome(tpl):
    return tpl == tpl[::-1]

# 25. Get Unique Elements
def unique_elements_tuple(tpl):
    seen = set()
    result = []
    for x in tpl:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return tuple(result)
