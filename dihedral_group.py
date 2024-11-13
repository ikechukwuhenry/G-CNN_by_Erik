class D4:

    @staticmethod
    def product(a: tuple, b: tuple) -> tuple:
        # Implements the *group law* of the group D_4.
        # The input `a` and `b` must be tuples containing two integers, e.g. `a = (f, r)`.
        # The two integeres indicate whether the group element includes a reflection and the number of rotations.
        # The method should return the tuple representing the product of the two input elements.
        # You should also check that the inputs are valid.

        ### BEGIN SOLUTION
        f_a, r_a = a
        f_b, r_b = b
        try:
            valid_f_a = int(f_a)
            valid_r_a = int(r_a)
            valid_f_b = int(f_b)
            valid_r_b = int(r_b)
        except ValueError:
            print("Invalid Inputs") 

        ### END SOLUTION

    @staticmethod
    def inverse(g: tuple) -> tuple:
        # Implements the *inverse* operation of the group D_4.
        # The input `g` must be a tuple containing two integers, e.g. `g = (f, r)`.
        # The two integeres indicate whether the group element includes a reflection and the number of rotations.
        # The method should return the tuple representing the inverse of the input element.
        # You should also check that the input is valid.

        ### BEGIN SOLUTION

        ### END SOLUTION
        pass