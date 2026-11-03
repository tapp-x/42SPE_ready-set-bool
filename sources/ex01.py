from operations import multiplier


def main():
    print(f"multiplier(0, 0) = {multiplier(0, 0)}")
    print(f"multiplier(0, 1) = {multiplier(0, 1)}")
    print(f"multiplier(1, 0) = {multiplier(1, 0)}")
    print(f"multiplier(1, 1) = {multiplier(1, 1)}")
    print(f"multiplier(2, 4) = {multiplier(2, 4)}")
    print(f"multiplier(5, 3) = {multiplier(5, 3)}")
    print(f"multiplier(7, 1) = {multiplier(7, 1)}")

    print("\n=== Invalid values ===")
    try:
        multiplier(-2, 3)
    except ValueError as error:
        print(f"Error (expected): {error}")

    try:
        multiplier(3, -2)
    except ValueError as error:
        print(f"Error (expected): {error}")

    try:
        multiplier(-2, -3)
    except ValueError as error:
        print(f"Error (expected): {error}")


if __name__ == "__main__":
    main()
