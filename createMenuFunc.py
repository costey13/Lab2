def createMenu(optList):
    """
    this function creates a menu from the string it was given
    """
    tmp = ""
    ct = 1
    for el in optList:
        tmp += str(ct) + ") " + el + '\n'
        ct += 1
    return tmp
