from operations import sat


def main():
    print(f"sat('AB|') = {sat('AB|')}")
    print(f"sat('AB&') = {sat('AB&')}")
    print(f"sat('AA!&') = {sat('AA!&')}")
    print(f"sat('AA^') = {sat('AA^')}")


if __name__ == "__main__":
    main()
