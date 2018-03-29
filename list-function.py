# this is how the list function works
def lister(thing):
    new_list = []
    for letter in thing:
        new_list.append(letter) 
    return new_list

new = lister("Shantel")
print(new)