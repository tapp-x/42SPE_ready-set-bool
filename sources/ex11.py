from operations import map, reverse_map


def main():
    coordinates = [(0, 0), (1, 0), (0, 1), (1, 1), (65535, 65535)]

    for x, y in coordinates:
        value = map(x, y)
        print(f"reverse_map(map({x}, {y})) = {reverse_map(value)}")


if __name__ == "__main__":
    main()
