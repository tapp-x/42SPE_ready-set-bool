from parsing import check_formula
from utils import combine_with_or, clauses_to_formula

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


def print_truth_table(formula: str):
    """Print the truth table of a formula written in reverse Polish notation."""
    operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    check_formula(formula, operands)

    variables = []
    for operand in operands:
        if operand in formula:
            variables.append(operand)

    number_of_variables = len(variables)
    number_of_rows = 1 << number_of_variables

    # Print the table header
    print("| " + " | ".join(variables) + " | = |")
    print("|" + "---|" * (number_of_variables + 1))

    for row_number in range(number_of_rows):
        variable_values = {}

        # Convert the row number into values for A, B, C, etc.
        for index, variable in enumerate(variables):
            bit_position = number_of_variables - index - 1
            bit = (row_number >> bit_position) & 1
            variable_values[variable] = bit == 1

        # Evaluate the formula with a stack.
        stack = []
        for char in formula:
            if char in variable_values:
                stack.append(variable_values[char])
            elif char == "!":
                value = stack.pop()
                stack.append(not value)
            else:
                right = stack.pop()
                left = stack.pop()

                if char == "&":
                    result = left and right
                elif char == "|":
                    result = left or right
                elif char == "^":
                    result = left != right
                elif char == ">":
                    result = not left or right
                elif char == "=":
                    result = left == right
                else:
                    raise ValueError("Invalid formula")

                stack.append(result)

        formula_result = stack.pop()
        row_values = []
        for variable in variables:
            row_values.append(str(int(variable_values[variable])))

        print("| " + " | ".join(row_values)
              + f" | {int(formula_result)} |")


def negation_normal_form(formula: str) -> str:
    """Return an equivalent formula in Negation Normal Form."""
    operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    check_formula(formula, operands)
    stack = []

    for char in formula:
        if char in operands:
            stack.append((char, char + "!"))
        elif char == "!":
            positive, negative = stack.pop()
            stack.append((negative, positive))
        else:
            right_positive, right_negative = stack.pop()
            left_positive, left_negative = stack.pop()

            if char == "&":
                positive = left_positive + right_positive + "&"
                negative = left_negative + right_negative + "|"
            elif char == "|":
                positive = left_positive + right_positive + "|"
                negative = left_negative + right_negative + "&"
            elif char == ">":
                positive = left_negative + right_positive + "|"
                negative = left_positive + right_negative + "&"
            elif char == "^":
                positive = (left_positive + right_negative + "&"
                            + left_negative + right_positive + "&|")
                negative = (left_positive + right_positive + "&"
                            + left_negative + right_negative + "&|")
            elif char == "=":
                positive = (left_positive + right_positive + "&"
                            + left_negative + right_negative + "&|")
                negative = (left_positive + right_negative + "&"
                            + left_negative + right_positive + "&|")
            else:
                raise ValueError("Invalid formula")

            stack.append((positive, negative))

    return stack.pop()[0]


def conjunctive_normal_form(formula: str) -> str:
    """Return an equivalent formula in Conjunctive Normal Form."""
    operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    check_formula(formula, operands)
    normal_formula = negation_normal_form(formula)
    stack = []
    index = 0

    while index < len(normal_formula):
        char = normal_formula[index]

        if char in operands:
            literal = char
            if index + 1 < len(normal_formula):
                if normal_formula[index + 1] == "!":
                    literal += "!"
                    index += 1
            stack.append([[literal]])
        elif char == "&":
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)
        elif char == "|":
            right = stack.pop()
            left = stack.pop()
            stack.append(combine_with_or(left, right))
        else:
            raise ValueError("Invalid formula")

        index += 1

    return clauses_to_formula(stack.pop())


def sat(formula: str) -> bool:
    """Return whether a Boolean formula is satisfiable."""
    operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    check_formula(formula, operands)

    variables = []
    for operand in operands:
        if operand in formula:
            variables.append(operand)

    number_of_variables = len(variables)
    number_of_rows = 1 << number_of_variables

    for row_number in range(number_of_rows):
        variable_values = {}
        for index, variable in enumerate(variables):
            bit_position = number_of_variables - index - 1
            bit = (row_number >> bit_position) & 1
            variable_values[variable] = bit == 1

        stack = []
        for char in formula:
            if char in variable_values:
                stack.append(variable_values[char])
            elif char == "!":
                stack.append(not stack.pop())
            else:
                right = stack.pop()
                left = stack.pop()

                if char == "&":
                    result = left and right
                elif char == "|":
                    result = left or right
                elif char == "^":
                    result = left != right
                elif char == ">":
                    result = not left or right
                elif char == "=":
                    result = left == right
                else:
                    raise ValueError("Invalid formula")

                stack.append(result)

        if stack.pop():
            return True

    return False


def powerset(set_values: list[int]) -> list[list[int]]:
    """Return all subsets of a set of integers."""
    result = []
    number_of_subsets = 1 << len(set_values)

    for mask in range(number_of_subsets):
        subset = []
        for index, value in enumerate(set_values):
            if (mask >> index) & 1:
                subset.append(value)
        result.append(subset)

    return result

