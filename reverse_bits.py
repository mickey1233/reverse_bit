def reversebits(n):
    n = '{:032b}'.format(n)
    n = n[::-1]
    print(int(n, 2))


def main():
    reversebits(int('00000010100101000001111010011100', 2))
    reversebits(int('11111111111111111111111111111101', 2))


if __name__ == "__main__":
    main()
