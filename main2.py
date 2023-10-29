from prettytable import  PrettyTable

class Students:
    newtable = PrettyTable(["ID", "FIO", "VARIANT", "GROUP"])
    f = open("god.txt", encoding='utf-8')
    for i in f:
        g = i.split(";")
        newtable.add_row([int(g[0]), g[1], int(g[2]), int(g[3])])
    print(newtable)


Students()


