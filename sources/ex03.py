from operations import eval_formula

def main():
    print(f"eval_formula('1') = {eval_formula('1')}")
    print(f"eval_formula('0') = {eval_formula('0')}")
    print(f"eval_formula('10&') = {eval_formula('10&')}")
    print(f"eval_formula('10|') = {eval_formula('10|')}")
    print(f"eval_formula('11>') = {eval_formula('11>')}")
    print(f"eval_formula('10=') = {eval_formula('10=')}")
    print(f"eval_formula('10^') = {eval_formula('10^')}")
    print(f"eval_formula('1011||=') = {eval_formula('1011||=')}")
    print(f"eval_formula('1!') = {eval_formula('1!')}")

    print("\n=== Invalid values ===")
    try:
        eval_formula("!")
    except ValueError as error:
        print(f"Error (expected): {error}")

    try:
        eval_formula("10")
    except ValueError as error:
        print(f"Error (expected): {error}")

    try:
        eval_formula("1&")
    except ValueError as error:
        print(f"Error (expected): {error}")


if __name__ == "__main__":
    main()
