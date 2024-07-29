class D4Element:
    def __init__(self, rotation=0, reflection=False):
        self.rotation = rotation % 4
        self.reflection = reflection

    def __mul__(self, other):
        if self.reflection:
            new_rotation = (self.rotation - other.rotation) % 4
        else:
            new_rotation = (self.rotation + other.rotation) % 4
        new_reflection = self.reflection != other.reflection
        return D4Element(new_rotation, new_reflection)

    def __eq__(self, other):
        return self.rotation == other.rotation and self.reflection == other.reflection

    def __repr__(self):
        return f"D4Element(rotation={self.rotation}, reflection={self.reflection})"


# Generate the elements of D4
elements = [
    D4Element(0, False),  # identity
    D4Element(1, False),  # 90 degrees rotation
    D4Element(2, False),  # 180 degrees rotation
    D4Element(3, False),  # 270 degrees rotation
    D4Element(0, True),   # reflection over vertical axis
    D4Element(1, True),   # reflection over diagonal 1
    D4Element(2, True),   # reflection over horizontal axis
    D4Element(3, True)    # reflection over diagonal 2
]

# Define a function to print the Cayley table
def print_cayley_table(elements):
    n = len(elements)
    table = [["" for _ in range(n)] for _ in range(n)]
    
    for i, e1 in enumerate(elements):
        for j, e2 in enumerate(elements):
            table[i][j] = e1 * e2
    
    print("Cayley Table:")
    for row in table:
        print(" | ".join(map(str, row)))
        
# Print the Cayley table
print_cayley_table(elements)