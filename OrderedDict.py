from collections import OrderedDict

if __name__ == "__main__":
    d = OrderedDict()
    for _ in range(int(input())):
        iname, _, iprice = input().rpartition(" ")
        d[iname] = d.get(iname, 0) + int(iprice)

    for key, value in d.items():
        print(key, value)
