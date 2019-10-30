# def contains():
#     if 2 in l:
#         return True
#     else:
#         return False


# l = [1, 2, 3, 7]
# print(contains())


# def contains(item, list):
#    '''
#    Returns `True` if item is in the list, `False` if it's not
#    '''
def contains(item, list):

    for i in list:
        if i == item:
            return True
        # else:
    return False


list = [1, 2, 3, 7]
print(contains(3, list))
