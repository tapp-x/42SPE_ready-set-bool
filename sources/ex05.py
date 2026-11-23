from operations import negation_normal_form


def main():
    print(negation_normal_form("AB&!"))
    print(negation_normal_form("AB|!"))
    print(negation_normal_form("AB>"))
    print(negation_normal_form("AB="))
    print(negation_normal_form("AB|C&!"))


if __name__ == "__main__":
    main()
