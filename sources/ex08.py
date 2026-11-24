from operations import powerset


def main():
    print(f"powerset([]) = {powerset([])}")
    print(f"powerset([1]) = {powerset([1])}")
    print(f"powerset([1, 2, 3]) = {powerset([1, 2, 3])}")


if __name__ == "__main__":
    main()
