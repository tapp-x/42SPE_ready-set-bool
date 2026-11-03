def check_formula(formula: str, operands: str):
    """Check that a reverse Polish formula has valid syntax."""
    stack_size = 0

    for char in formula:
        if char in operands:
            stack_size += 1
        elif char == "!":
            if stack_size < 1:
                raise ValueError("Invalid formula")
        elif char in "&|^>=":
            if stack_size < 2:
                raise ValueError("Invalid formula")
            stack_size -= 1
        else:
            raise ValueError("Invalid formula")

    if stack_size != 1:
        raise ValueError("Invalid formula")
