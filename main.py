from sh_ya_alg import reverse


def main():
    expression = input("Write an expression: ")
    print('-'*20, '\n', "End result is ", " ".join(str(e) for e in reverse(expression)))


if __name__ == '__main__':
    main()