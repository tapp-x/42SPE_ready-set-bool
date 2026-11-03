from operations import gray_code

def main():
    print(f"gray_code(0) = {gray_code(0)}")
    print(f"gray_code(1) = {gray_code(1)}")
    print(f"gray_code(2) = {gray_code(2)}")
    print(f"gray_code(3) = {gray_code(3)}")
    print(f"gray_code(4) = {gray_code(4)}")
    print(f"gray_code(5) = {gray_code(5)}")
    print(f"gray_code(6) = {gray_code(6)}")
    print(f"gray_code(7) = {gray_code(7)}")
    print(f"gray_code(8) = {gray_code(8)}")
    print(f"gray_code(9) = {gray_code(9)}")
    print(f"gray_code(10) = {gray_code(0)}")
    print(f"gray_code(11) = {gray_code(1)}")
    print(f"gray_code(12) = {gray_code(2)}")

    print("\n=== Invalid values ===")
    try:
        gray_code(-1)
    except ValueError as error:
        print(f"Error (expected): {error}")


if __name__ == "__main__":
    main()