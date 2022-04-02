import os

def chooseTemplate():
    templates = [ i for i in os.listdir() if i[-3:] == "xml"]

    print("----------Choose template----------")
    for i, j in enumerate(templates):
        print(f"[{i}] - {j[:-4]}")
    
    choose = int(input("Choice: "))
    while choose >= len(templates) or choose < 0:
        choose = int(input("Choice: "))

    return templates[choose]


def getTasksCount():
    print("Enter your tasks count: ")
    
    counts = int(input())
    while counts < 1:
        counts = int(input())
    
    return counts


def getReportName():
    print("Enter your report name: ")
    name = input()

    while len(name.strip()) == 0:
        print("Enter your report name: ")
        name = input()

    return name


def getString(invite):
    print(invite)

    return input()