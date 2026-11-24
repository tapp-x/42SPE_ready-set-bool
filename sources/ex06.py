from operations import conjunctive_normal_form


def main():
    print(conjunctive_normal_form("AB&!"))
    print(conjunctive_normal_form("AB|!"))
    print(conjunctive_normal_form("AB|C&"))
    print(conjunctive_normal_form("AB|C|D|"))
    print(conjunctive_normal_form("AB&C&D&"))
    print(conjunctive_normal_form("AB&!C!|"))
    print(conjunctive_normal_form("AB|!C!&"))
    print(conjunctive_normal_form("ABCD&|&"))


if __name__ == "__main__":
    main()
