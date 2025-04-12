# 1. Get Value
def get_value(d, key):
    return d.get(key, "Key not found")

# 2. Check Key
def check_key_exists(d, key):
    return key in d

# 3. Count Keys
def count_keys(d):
    return len(d)

# 4. Get All Keys
def get_all_keys(d):
    return list(d.keys())

# 5. Get All Values
def get_all_values(d):
    return list(d.values())

# 6. Merge Dictionaries
def merge_dictionaries(d1, d2):
    return {**d1, **d2}

# 7. Remove Key
def remove_key(d, key):
    d.pop(key, None)
    return d

# 8. Clear Dictionary
def clear_dictionary():
    return {}

# 9. Check if Dictionary is Empty
def is_dict_empty(d):
    return len(d) == 0

# 10. Get Key-Value Pair
def get_key_value_pair(d, key):
    return (key, d[key]) if key in d else "Key not found"

# 11. Update Value
def update_value(d, key, new_value):
    if key in d:
        d[key] = new_value
    return d

# 12. Count Value Occurrences
def count_value_occurrences(d, value):
    return list(d.values()).count(value)

# 13. Invert Dictionary
def invert_dictionary(d):
    return {v: k for k, v in d.items()}

# 14. Find Keys with Value
def find_keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]

# 15. Create a Dictionary from Lists
def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

# 16. Check for Nested Dictionaries
def has_nested_dict(d):
    return any(isinstance(v, dict) for v in d.values())

# 17. Get Nested Value
def get_nested_value(d, outer_key, inner_key):
    return d.get(outer_key, {}).get(inner_key, "Key not found")

# 18. Create Default Dictionary
from collections import defaultdict
def create_default_dict(default_type):
    return defaultdict(default_type)

# 19. Count Unique Values
def count_unique_values(d):
    return len(set(d.values()))

# 20. Sort Dictionary by Key
def sort_dict_by_key(d):
    return dict(sorted(d.items()))

# 21. Sort Dictionary by Value
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

# 22. Filter by Value
def filter_dict_by_value(d, condition):
    return {k: v for k, v in d.items() if condition(v)}

# 23. Check for Common Keys
def has_common_keys(d1, d2):
    return not set(d1.keys()).isdisjoint(d2.keys())

# 24. Create Dictionary from Tuple
def dict_from_tuple_list(tuples):
    return dict(tuples)

# 25. Get the First Key-Value Pair
def get_first_key_value(d):
    return next(iter(d.items()), None)
