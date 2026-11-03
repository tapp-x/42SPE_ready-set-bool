from parsing import check_formula


def adder(a: int, b: int) -> int:
    """Return the sum of two natural numbers using bitwise operations."""
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

def multiplier(a: int, b: int) -> int:
    """Return the product of two natural numbers using bitwise operations."""
    if a < 0:
        raise ValueError("a must be non-negative")
    if b < 0:
        raise ValueError("b must be non-negative")

    result = 0
    while b != 0:
        if (b & 1) == 1:
            result = adder(result, a)
        a = a << 1
        b = b >> 1
    return result

def gray_code(n: int) -> int:
    """Return the Gray code of a natural number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return n ^ (n >> 1)


def eval_formula(formula: str) -> bool:
    """Evaluate a Boolean formula written in reverse Polish notation."""
    check_formula(formula, "01")
    stack = []

    for char in formula:
        if char == "0":
            stack.append(False)
        elif char == "1":
            stack.append(True)
        elif char == "!":
            stack.append(not stack.pop())
        else:
            first_pop = stack.pop()
            second_pop = stack.pop()

            if char == "&":
                result = second_pop and first_pop
            elif char == "|":
                result = second_pop or first_pop
            elif char == "^":
                result = second_pop != first_pop
            elif char == ">":
                result = not second_pop or first_pop
            else:
                result = second_pop == first_pop

            stack.append(result)

    return stack.pop()

