from operations import eval_set


def main():
    sets = [[0, 1, 2], [0, 3, 4]]
    print(f"eval_set('AB&', {sets}) = {eval_set('AB&', sets)}")

    sets = [[0, 1, 2], [3, 4, 5]]
    print(f"eval_set('AB|', {sets}) = {eval_set('AB|', sets)}")

    sets = [[0, 1, 2]]
    print(f"eval_set('A!', {sets}) = {eval_set('A!', sets)}")

    sets = [[1], [2], [1, 3]]
    print(f"eval_set('AC&', {sets}) = {eval_set('AC&', sets)}")


if __name__ == "__main__":
    main()
