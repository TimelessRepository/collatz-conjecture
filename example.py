from CollatzConjecture import CollatzConjecture

# 1 int param -> give the number sequence
print(CollatzConjecture(9))
print()

# 2 int param -> give the numbers sequence of the range
print(CollatzConjecture(1,11))
print()

# 1 tuple param -> give the numbers sequence of the range but with tuple or list
A = CollatzConjecture([1,11])
print(A)
print()

# fullDescription -> get all sequence and the elapsed time (for testing)
print(A.fullDescription())
print()

# generator -> get a generator for a single o more sequences
for n in A.generator():
    print(n)