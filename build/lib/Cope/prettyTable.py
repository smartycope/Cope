from .imports import dependsOnPackage

#* PrettyTable
@dependsOnPackage('prettytable', 'PrettyTable')
def quickTable(listOfLists, interpretAsRows=True, fieldNames=None, returnStr=False, sortByField:str=False, sortedReverse=False):
    """ A small, quick wrapper for the prettytable library """
    t = PrettyTable()
    if interpretAsRows:
        if fieldNames is not None:
            t.field_names = fieldNames
        t.add_rows(listOfLists)
    else:
        if fieldNames is not None:
            for i, name in zip(listOfLists, fieldNames):
                t.add_column(name, i)
        else:
            for i in listOfLists:
                t.add_column(str(i[0]), i[1:])

    if sortByField:
        t.sortby = sortByField
        t.reversesort = sortedReverse

    return t.get_string() if returnStr else t
