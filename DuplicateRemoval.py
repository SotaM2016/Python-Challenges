def removeDups(list):
    newlist = []
    for item in list:
        if item not in newlist:
            newlist.append(item)
    return newlist


print(removeDups(['test', 'test2', 'test', 'test3', 'test4']))