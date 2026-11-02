def adder(a: int, b: int) -> int:
    """Return the sum of two natural numbers using bitwise operations."""
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
