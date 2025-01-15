# Given two sets, demonstrate union, intersection, and difference.
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union of set_a and set_b
union_result = set_a.union(set_b)
# Alternatively, you can use the | operator: union_result = set_a | set_b

# Intersection of set_a and set_b
intersection_result = set_a.intersection(set_b)
# Alternatively, you can use the & operator: intersection_result = set_a & set_b

# Difference of set_a and set_b (elements in set_a but not in set_b)
difference_result_a_b = set_a.difference(set_b)
difference_result_b_a = set_b.difference(set_a)

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union of A and B: {union_result}")
print(f"Intersection of A and B: {intersection_result}")
print(f"Difference of A and B (A - B): {difference_result_a_b}")
print(f"Difference of B and A (B - A): {difference_result_b_a}")