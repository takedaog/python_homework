# 1. Union of Sets
def union_sets(set1, set2):
    return set1 | set2

# 2. Intersection of Sets
def intersection_sets(set1, set2):
    return set1 & set2

# 3. Difference of Sets
def difference_sets(set1, set2):
    return set1 - set2

# 4. Check Subset
def is_subset(set1, set2):
    return set1.issubset(set2)

# 5. Check Element
def check_element_set(s, element):
    return element in s

# 6. Set Length
def length_of_set(s):
    return len(s)

# 7. Convert List to Set
def list_to_set(lst):
    return set(lst)

# 8. Remove Element
def remove_element_set(s, element):
    s.discard(element)
    return s

# 9. Clear Set
def clear_set(s):
    s.clear()
    return s

# 10. Check if Set is Empty
def is_set_empty(s):
    return len(s) == 0

# 11. Symmetric Difference
def symmetric_difference_sets(set1, set2):
    return set1 ^ set2

# 12. Add Element
def add_element_set(s, element):
    s.add(element)
    return s

# 13. Pop Element
def pop_element_set(s):
    return s.pop() if s else None

# 14. Find Maximum
def max_element_set(s):
    return max(s)

# 15. Find Minimum
def min_element_set(s):
    return min(s)

# 16. Filter Even Numbers
def filter_even_set(s):
    return {x for x in s if x % 2 == 0}

# 17. Filter Odd Numbers
def filter_odd_set(s):
    return {x for x in s if x % 2 != 0}

# 18. Create a Set of a Range
def create_range_set(start, end):
    return set(range(start, end + 1))

# 19. Merge and Deduplicate
def merge_and_deduplicate_lists(lst1, lst2):
    return set(lst1 + lst2)

# 20. Check Disjoint Sets
def are_sets_disjoint(set1, set2):
    return set1.isdisjoint(set2)

# 21. Remove Duplicates from a List
def remove_duplicates_list(lst):
    return list(set(lst))

# 22. Count Unique Elements
def count_unique_elements(lst):
    return len(set(lst))

# 23. Generate Random Set
import random
def generate_random_set(count, start, end):
    return set(random.sample(range(start, end + 1), min(count, end - start + 1)))
