def print_formatted(number):
    # your code goes here
    space = len(bin(number)) - 2
    for i in range(1, number + 1):
        deci = str(i)
        octal = str(oct(i))[2:]
        hexa = hex(i)[2:].upper()
        bi = str(bin(i))[2:]
        print(deci.rjust(space), octal.rjust(space), hexa.rjust(space), bi.rjust(space))


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
