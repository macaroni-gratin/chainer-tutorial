print("ans 1")
a = [4, 8, 3, 4, 1]
odd_or_even = [x % 2 for x in a]
print(odd_or_even)

print("ans 2")
print(sum(x == 1 for x in odd_or_even))

print("ans 3")
print([x for x in a if x%2 == 1])
