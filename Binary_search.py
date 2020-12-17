#naive search
def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i

    return -1

#binary search
def binary_search(list, target):
    mid_point = len(list) // 2
    if list[mid_point] == target:
        return mid_point

    elif list[mid_point] > target:
        return binary_search(list[:mid_point], target)

    else:
        return binary_search(list[mid_point + 1:], target)

        