from operations import adder


def main():
    print(f"adder(0, 0) = {adder(0, 0)}")
    print(f"adder(1, 1) = {adder(1, 1)}")
    print(f"adder(5, 3) = {adder(5, 3)}")
    print(f"adder(7, 1) = {adder(7, 1)}")
    print(f"adder(0xFFFFFFFF, 1) = {adder(0xFFFFFFFF, 1)}")

    print("\n=== Invalid values ===")
    try:
        adder(-1, 1)
    except ValueError as error:
        print(f"Error (expected): {error}")

    try:
        adder(0x100000000, 0)
    except ValueError as error:
        print(f"Error (expected): {error}")


if __name__ == "__main__":
    main()
