from parsing import check_formula

MAX_U32 = 0xFFFFFFFF


def adder(a: int, b: int) -> int:
    """Return the sum of two natural numbers using bitwise operations."""
    if a < 0 or a > MAX_U32:
        raise ValueError("a must fit in u32")
    if b < 0 or b > MAX_U32:
        raise ValueError("b must fit in u32")

    while b != 0:
        carry = a & b
        a = (a ^ b) & MAX_U32
        b = (carry << 1) & MAX_U32
    return a

def multiplier(a: int, b: int) -> int:
    """Return the product of two natural numbers using bitwise operations."""
    if a < 0 or a > MAX_U32:
        raise ValueError("a must fit in u32")
    if b < 0 or b > MAX_U32:
        raise ValueError("b must fit in u32")

    result = 0
    while b != 0:
        if (b & 1) == 1:
            result = adder(result, a)
        a = (a << 1) & MAX_U32
        b = b >> 1
    return result

def gray_code(n: int) -> int:
    """Return the Gray code of a natural number."""
    if n < 0 or n > MAX_U32:
        raise ValueError("n must fit in u32")
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

