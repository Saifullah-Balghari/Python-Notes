countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)  # tuples cant be changed so convert it to a list,make changes and revert it to tuple.
temp.append("Russia")  # add item
temp.pop(3)  # remove item
temp[2] = "Finland"  # change item
countries = tuple(temp)
print(countries)
