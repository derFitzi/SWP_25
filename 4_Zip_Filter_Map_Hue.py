def main():
    names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
    ages = [23, 17, 34, 15, 29]
    scores = [88, 92, 75, 64, 91]
    zippedList = tuple(zip(names, ages, scores))
    filteredTupleLamda =list(filter(lambda x: x[1] >= 18 and x[2] >= 80, zippedList))
    mappedDict = list(map(lambda x: {"name": x[0], "age":x[1], "score": x[2]}, filteredTupleLamda)) #Liste mit Dicts (sinnvoll?)

    print(zippedList)
    print(filteredTupleLamda)
    print(mappedDict)


if __name__ == "__main__":
    main()


