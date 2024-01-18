import random
from fractions import Fraction

pairs = []

while len(pairs) < 20:
    a = random.randint(-10, 10)
    if a != 0:
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        pairs.append((a, b, c))

for idx, pair in enumerate(pairs, 1):
    a_str = f"+{pair[0]}" if pair[0] > 0 else pair[0]
    b_str = f"+{pair[1]}" if pair[1] >= 0 else pair[1]
    c_str = f"+{pair[2]}" if pair[2] >= 0 else pair[2]

    vertex_x = Fraction(-pair[1], 2 * pair[0])
    vertex_y = Fraction(pair[2] - (pair[1] ** 2), 4 * pair[0])

    print(f"y={pair[0]}x^2{b_str}x{c_str}, ({vertex_x}, {vertex_y})")