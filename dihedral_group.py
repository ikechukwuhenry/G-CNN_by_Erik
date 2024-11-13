class D4:

  @staticmethod
  def product(a: tuple, b: tuple) -> tuple:
    # Implements the *group law* of the group D_4.
    # The input `a` and `b` must be tuples containing two integers, e.g. `a = (f, r)`.
    # The two integeres indicate whether the group element includes a reflection and the number of rotations.
    # The method should return the tuple representing the product of the two input elements.
    # You should also check that the inputs are valid.

    ### BEGIN SOLUTION
    try:
      valid_a = (int(a[0]), int(a[1]))
      valid_b = (int(b[0]), int(b[1]))
      if valid_a[0] == 0 and valid_b[0] == 0:
        return (0, (valid_a[1] + valid_b[1]) % 4)
      elif valid_a[0] == 1 and valid_b[0] == 1:
        return (0, (valid_a[1] - valid_b[1]) % 4)
      elif valid_a[0] == 0 and valid_b[0] == 1:
        return (1, (valid_a[1] + valid_b[1]) % 4)
      else:
        return (1, (valid_a[1] - valid_b[1]) % 4)
    except ValueError:
      print('Invalid input')
    ### END SOLUTION
  
  @staticmethod
  def inverse(g: int) -> int:
    # Implements the *inverse* operation of the group D_4.
    # The input `g` must be a tuple containing two integers, e.g. `g = (f, r)`.
    # The two integeres indicate whether the group element includes a reflection and the number of rotations.
    # The method should return the tuple representing the inverse of the input element.
    # You should also check that the input is valid.

    ### BEGIN SOLUTION
    try:
      valid_g = (int(g[0]), int(g[1]))
      if valid_g[0] == 0:
        return (valid_g[0], (4 - valid_g[1]) % 4)
      else:
        return (1, (4 - valid_g[1]) % 4)
    except ValueError:
      print('Invalid input')
    ### END SOLUTION



e = (0, 0) # the identity element
f = (1, 0) # the horizontal reflection
r = (0, 1) # the rotation by 90 degrees

# Let's verify that the implementation is consistent with the instructions given
assert D4.product(e, e) == e
assert D4.product(f, f) == e
assert D4.product(f, r) == D4.product(D4.inverse(r), f)

# Let's verify that the implementation satisfies the group axioms
a = (1, 2)
b = (0, 3)
c = (1, 1)
assert D4.product(a, e) == a
assert D4.product(e, a) == a
assert D4.product(b, D4.inverse(b)) == e
assert D4.product(D4.inverse(b), b) == e

assert D4.product(D4.product(a, b), c) == D4.product(a, D4.product(b, c))

print(D4.product(D4.product(a, b), c))
print(D4.product(a, D4.product(b, c)))