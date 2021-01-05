if __name__ == "__main__":
    st = input()
    newstring = ""

    for i in st:
        if (i.islower()) == True:
            newstring += i.upper()
        elif (i.isupper()) == True:
            newstring += i.lower()
        else:
            newstring += i

    print(newstring)
