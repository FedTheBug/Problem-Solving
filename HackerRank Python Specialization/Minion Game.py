def minion_game(string):
    # your code goes here
    Stuart = 0
    Kevin = 0
    vowels = "AEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i
    if Kevin > Stuart:
        print("Kevin {}".format(Kevin))
    elif Kevin == Stuart:
        print("Draw")
    else:
        print("Stuart {}".format(Stuart))


if __name__ == "__main__":
    s = input()
    minion_game(s)
